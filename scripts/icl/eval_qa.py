import argparse
import os
import csv
import json
import random
from tqdm import tqdm
import wandb
import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset, Dataset, DatasetDict
from evaluate import load

squad_metric = load("squad")


CACHE_DIR = "/gscratch/argon/kahuja/.cache/"
DATA_DIR = "data/Question-Answering/SDQA-gold-task"
MODEL2HFSTR = {"mistral": "mistralai/Mistral-7B-v0.1"}


def load_datasets(lang):
    datasets = {}
    for split in ["train", "test", "validation"]:
        filename = f"{DATA_DIR}/sdqa_{split}_{lang}.json"
        with open(filename) as f:
            dataset = json.load(f)["data"]
        rows = []
        for i in range(len(dataset)):
            paragraphs = dataset[i]["paragraphs"]
            for j in range(len(paragraphs)):
                context = paragraphs[j]["context"]
                qas = paragraphs[j]["qas"]
                for k in range(len(qas)):
                    question = qas[k]["question"]
                    answer = qas[k]["answers"][0]["text"]
                    answers_full = qas[k]["answers"]
                    qid = qas[k]["id"]
                    rows.append([context, question, answer, answers_full, qid])
        datasets[split] = pd.DataFrame(rows)
        datasets[split].columns = [
            "context",
            "question",
            "answer",
            "answers_full",
            "qid",
        ]
        datasets[split] = Dataset.from_pandas(datasets[split])

    datasets = DatasetDict(datasets)
    return datasets


def get_few_shot_examples(dataset, k=2, seed=42):
    few_shot_examples = []
    shuffled = dataset.shuffle(seed=seed)
    shuffled = shuffled.select(range(min(k, len(shuffled))))
    few_shot_examples += [example for example in shuffled]
    return few_shot_examples


def generate(model, tokenizer, prompt, device, max_tokens=20, temperature=1.0):
    tokenized_out = tokenizer(prompt, return_tensors="pt")
    input_ids = tokenized_out["input_ids"].to(device)
    with torch.no_grad():
        output = model(input_ids, max_new_tokens=max_tokens, temperature=temperature)
    generated_text = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    prefix_to_remove = prompt
    if generated_text.startswith(prefix_to_remove):
        generated_text = generated_text[len(prefix_to_remove) :].strip()
    #     generated_text = generated_text.split("\n\n")[0].split("Label:")[-1].strip()

    return generated_text


def process_text(text):
    return text.lower()


def process_generation(text):
    return text.split("\n\n")[0].strip().lower()


def construct_prompt(test_example, fs_examples):
    def example_to_prompt(example, add_label=True):
        ex_prompt = (
            f"Passage: {example['context']}\nQuestion: {example['question']}\nAnswer:"
        )
        if add_label:
            ex_prompt += f" {example['answer']}"
        return ex_prompt

    instruction = "This task is about writing a correct answer for the reading comprehension task. Based on the information provided in a given passage, you should identify the shortest continuous text span from the passage that serves as an answer to the given question. Avoid answers that are incorrect or provides incomplete justification for the question."
    prompt = instruction
    for example in fs_examples:
        prompt += "\n\n" + example_to_prompt(example, add_label=True)

    prompt += "\n\n" + example_to_prompt(test_example, add_label=False)
    return prompt


def evaluate_generation(generated_text, test_example):
    predictions = [{"prediction_text": generated_text, "id": test_example["qid"]}]

    answers = {
        "answer_start": [],
        "text": [],
    }
    for answer in test_example["answers_full"]:
        answers["answer_start"].append(answer["answer_start"])
        answers["text"].append(answer["text"])
    references = [{"answers": answers, "id": test_example["qid"]}]
    return squad_metric.compute(predictions=predictions, references=references)


def evaluate_model(model, tokenizer, test_prompts, device):
    preds = []
    f1s = []
    ems = []
    for test_prompt in tqdm(test_prompts):
        generated_text = generate(
            model, tokenizer, test_prompt["prompt"], device=device
        )
        preds.append(process_text(generated_text))
        result = evaluate_generation(generated_text, test_prompt["example"])
        f1s.append(result["f1"])
        ems.append(result["exact"])

    return np.mean(f1s), np.mean(ems), preds, f1s, ems


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def prepare_out_file(ids, preds, f1s, ems, split, save_dir):
    out_file = f"{save_dir}/{split}_results.csv"
    with open(out_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["pred", "f1", "em"])
        for id, pred, f1, em in zip(ids, preds, f1s, ems):
            writer.writerow([id, pred, f1, em])
    return out_file


def eval(dataset, fs_examples, split, model, tokenizer, device, save_dir=None):
    test_prompts = [
        {
            "prompt": construct_prompt(test_example, fs_examples),
            "example": test_example,
        }
        for test_example in dataset[split]
    ]

    f1, em, preds, f1s, ems = evaluate_model(
        model, tokenizer, test_prompts, device=device
    )
    ids = [test_example["qid"] for test_example in dataset[split]]
    out_file = prepare_out_file(ids, preds, f1s, ems, split, save_dir)
    return f1, em, out_file


def main(args):
    set_seed(args.seed)
    save_dir = os.path.join(
        args.save_dir,
        args.lang,
        args.model,
        f"k_{args.k}",
        f"temperature_{args.temperature}",
        f"seed_{args.seed}",
    )

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    datasets = load_datasets(args.lang)
    model = AutoModelForCausalLM.from_pretrained(args.model, cache_dir=CACHE_DIR)
    tokenizer = AutoTokenizer.from_pretrained(args.model, cache_dir=CACHE_DIR)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    fs_examples = get_few_shot_examples(
        datasets["train"], k=args.few_shot_size, seed=args.seed
    )
    print("Evaluating on test data")
    f1, em, out_file = eval(
        datasets, fs_examples, "test", model, tokenizer, device, save_dir=save_dir
    )
    print(f"F1: {f1}, EM: {em}")
    print(f"Predictions saved in {out_file}")
    config = vars(args)
    config["metrics"] = {"f1": f1, "em": em}

    with open(os.path.join(save_dir, "results.json"), "w") as f:
        json.dump(config, f)

    wandb.log(
        {
            "f1": f1,
            "em": em,
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--lang",
        type=str,
        choices=[
            "english-gbr",
            "arabic-sau",
            "arabic-bhr",
            "english-phl",
            "arabic-egy",
            "korean-kors",
            "arabic-jor",
            "english-ind_s",
            "arabic-mar",
            "bengali-dhaka",
            "swahili-kenya",
            "swahili-tanzania",
            "english-zaf",
            "bengali-ind",
            "arabic-dza",
            "english-aus",
            "korean-korn",
            "arabic-tun",
            "english-ind_n",
            "english-nga",
            "english-nzl",
            "english-irl",
            "english-usa",
            "english-kenya",
        ],
        default="en",
    )
    parser.add_argument(
        "-m", "--model", type=str, default="mistral", choices=MODEL2HFSTR.keys()
    )
    parser.add_argument("--save_dir", type=str, default="results/qa")
    parser.add_argument("-k", "--few_shot_size", type=int, default=2)
    parser.add_argument("-t", "--temperature", type=float, default=1.0)
    parser.add_argument("-s", "--seed", type=int, default=42)
    args = parser.parse_args()

    wandb.init(
        project="dialect-bench",
        group="qa",
        name=f"{args.lang}_{args.model}_k{args.few_shot_size}_t{args.temperature}_s{args.seed}",
        config=vars(args),
    )

    main(args)
