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
from transformers import logging

logging.set_verbosity_error()

CACHE_DIR = "/gscratch/argon/kahuja/.cache/"
DATA_DIR = "data/sentiment_analysis/arabic/"
MODEL2HFSTR = {"mistral": "mistralai/Mistral-7B-v0.1"}


def load_datasets(lang):
    datasets = {}
    for split in ["train", "test", "validation"]:
        datasets[split] = pd.read_csv(
            os.path.join(DATA_DIR, lang, f"{split}.csv"), header=None
        )
        datasets[split].columns = ["text", "label"]
        datasets[split] = Dataset.from_pandas(datasets[split])
        datasets[split] = datasets[split].filter(
            lambda example: not (
                example["text"] == "sentence" and example["label"] == "label"
            )
        )
        print(f"{split} size: {len(datasets[split])}")

    datasets = DatasetDict(datasets)

    return datasets


def get_few_shot_examples(dataset, fs_per_label=4, seed=42):
    labels = list(set(dataset["label"]))
    few_shot_examples = []
    for label in labels:
        label_examples = dataset.filter(lambda example: example["label"] == label)
        # shuffle the examples
        label_examples = label_examples.shuffle(seed=seed)
        # get the first fs_per_label examples
        label_examples = label_examples.select(
            range(min(fs_per_label, len(label_examples)))
        )
        few_shot_examples += [example for example in label_examples]

    # Shuffle the few shot examples
    random.shuffle(few_shot_examples)
    return few_shot_examples


def get_neg_log_prob(model, tokenizer, prompt, device):
    model.eval()
    tokenized_out = tokenizer(prompt, return_tensors="pt")
    input_ids = tokenized_out["input_ids"].to(device)
    labels = input_ids

    with torch.no_grad():
        output = model(input_ids, labels=labels)

    return output.loss


def generate(model, tokenizer, prompt, device, max_tokens=20, temperature=1.0):
    tokenized_out = tokenizer(prompt, return_tensors="pt")
    input_ids = tokenized_out["input_ids"].to(device)
    attn_mask = tokenized_out["attention_mask"].to(device)
    labels = tokenized_out["input_ids"].to(device)
    with torch.no_grad():
        output = model.generate(
            input_ids,
            attention_mask=attn_mask,
            max_new_tokens=max_tokens,
            temperature=temperature,
        )
    generated_text = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    prefix_to_remove = prompt
    if generated_text.startswith(prefix_to_remove):
        generated_text = generated_text[len(prefix_to_remove) :].strip()
    #     generated_text = generated_text.split("\n\n")[0].split("Label:")[-1].strip()

    return generated_text


def evaluate_model_nll(model, tokenizer, test_prompts):
    preds = []
    acc = 0
    for test_prompt in tqdm(test_prompts, total=len(test_prompts)):
        neg_log_probA = get_neg_log_prob(
            model, tokenizer, test_prompt["correct_prompt"]
        )
        neg_log_probB = get_neg_log_prob(
            model, tokenizer, test_prompt["incorrect_prompt"]
        )
        if neg_log_probA < neg_log_probB:
            acc += 1
    acc = acc / len(test_prompts)

    return acc


def process_text(text):
    #     return text.split("Label:")[-1].strip().lower()
    return text.lower()


def process_generation(generation):
    return generation.split("\n\n")[0].split("Label:")[-1].strip().lower()


def evaluate_generation(generated_text, label):
    return float(process_generation(generated_text) == process_text(label))


def prepare_out_file(dataset, preds, correct_or_not, split, save_dir):
    for idx, (example, pred, match) in enumerate(zip(dataset, preds, correct_or_not)):
        text = example["text"]
        label = example["label"]
        with open(os.path.join(save_dir, f"{split}_out.csv"), "w") as f:
            csv_writer = csv.writer(f)
            if idx == 0:
                csv_writer.writerow(["text", "label", "pred", "match"])
            csv_writer.writerow([text, label, pred, match])


def evaluate_model_gen(
    model, tokenizer, test_prompts, device, save_file=None, overwrite_cache=False
):
    if save_file is not None and os.path.exists(save_file) and not overwrite_cache:
        cached_out = pd.read_csv(save_file)
        preds_cache = cached_out["pred"].tolist()
        correct_or_not_cache = cached_out["match"].tolist()

    else:
        preds_cache = []
        correct_or_not_cache = []

    if save_file is not None:
        f = open(save_file, "w" if overwrite_cache else "a")
        cache_writer = csv.writer(f)
        cache_writer.writerow(["text", "label", "pred", "match"])
    else:
        cache_writer = None

    preds = []
    correct_or_not = []
    accs = 0
    cache_size = len(preds_cache)
    try:
        for idx, test_prompt in tqdm(enumerate(test_prompts)):
            if idx < cache_size:
                preds.append(preds_cache[idx])
                correct_or_not.append(correct_or_not_cache[idx])
            else:
                generated_text = generate(
                    model,
                    tokenizer,
                    test_prompt["prompt"],
                    device=device,
                )
                preds.append(process_generation(generated_text))
                correct_or_not.append(
                    evaluate_generation(generated_text, test_prompt["label"])
                )

            if save_file is not None:
                if idx >= cache_size:
                    cache_writer.writerow(
                        [
                            test_prompt["text"],
                            test_prompt["label"],
                            preds[-1],
                            correct_or_not[-1],
                        ]
                    )
        if save_file is not None:
            f.close()

        return np.mean(correct_or_not), preds, correct_or_not

    except Exception as e:
        if save_file is not None:
            f.close()
        raise e


def construct_prompt(test_example, fs_examples, prompt_for_each_label=False, labels=[]):
    def example_to_prompt(example, add_label=True):
        ex_prompt = f"Sentence: {example['text']}\n"
        if add_label:
            ex_prompt += f"Label: {example['label']}\n"
        return ex_prompt

    # To Do: Add domain of the text in the instruction like "In this task you given text from {domain}"
    prompt = "In this task, you are given a piece of text. Your task is to classify the sentiment of the text based on its content.\n"

    for example in fs_examples:
        prompt += example_to_prompt(example, add_label=True)
        prompt += "\n"

    if not prompt_for_each_label:
        prompt += example_to_prompt(test_example, add_label=False)
        return prompt
    else:
        prompts = [
            prompt + example_to_prompt(test_example, add_label=True) for label in labels
        ]
        gold_label_idx = labels.index(test_example["label"])
        return prompts, gold_label_idx


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def eval(
    dataset,
    fs_examples,
    split,
    model,
    tokenizer,
    device,
    save_dir=None,
    overwrite_cache=False,
):
    test_prompts = [
        {
            "prompt": construct_prompt(test_example, fs_examples),
            "text": test_example["text"],
            "label": test_example["label"],
        }
        for test_example in dataset
    ]

    acc, preds, correct_or_not = evaluate_model_gen(
        model,
        tokenizer,
        test_prompts,
        device=device,
        save_file=os.path.join(save_dir, f"{split}_out.csv"),
        overwrite_cache=overwrite_cache,
    )
    # if save_dir is not None:
    #     prepare_out_file(dataset, preds, correct_or_not, split, save_dir)

    return acc


def main(args):
    set_seed(args.seed)

    save_dir = os.path.join(
        args.save_dir,
        args.lang,
        args.model,
        f"k{args.fs_per_label}",
        f"t{args.temperature}",
        f"s{args.seed}",
    )
    if args.debug:
        save_dir = os.path.join(save_dir, "debug")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    datasets = load_datasets(args.lang)
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL2HFSTR[args.model], cache_dir=CACHE_DIR
    )
    tokenizer.pad_token_id = tokenizer.eos_token_id
    model = AutoModelForCausalLM.from_pretrained(
        MODEL2HFSTR[args.model], cache_dir=CACHE_DIR
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    fs_examples = get_few_shot_examples(datasets["train"], args.fs_per_label, args.seed)
    # print("Evaluating on validation set")
    # val_acc = eval(
    #     datasets["validation"]
    #     if not args.debug
    #     else datasets["validation"].select(range(10)),
    #     fs_examples,
    #     "validation",
    #     model,
    #     tokenizer,
    #     device,
    #     save_dir=save_dir,
    #     overwrite_cache=args.overwrite_cache,
    # )
    print("Evaluating on test set")
    test_acc = eval(
        datasets["test"] if not args.debug else datasets["test"].select(range(10)),
        fs_examples,
        "test",
        model,
        tokenizer,
        device,
        save_dir=save_dir,
        overwrite_cache=args.overwrite_cache,
    )

    config = vars(args)
    config["metrics"] = {
        # "val_acc": val_acc,
        "test_acc": test_acc,
    }
    with open(os.path.join(save_dir, "results.json"), "w") as f:
        json.dump(config, f)

    wandb.log(
        {
            # "val_acc": val_acc,
            "test_acc": test_acc,
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--lang",
        default="aeb_Arab",
        type=str,
        choices=[
            "aeb_Arab",
            "aeb_Latn",
            "ar_lb",
            "arb_arab",
            "arq_arab",
            "ary_arab",
            "arz_arab",
            "jor_arab",
            "sau_arab",
        ],
    )
    parser.add_argument("-m", "--model", default="mistral", choices=MODEL2HFSTR.keys())
    parser.add_argument("-s", "--seed", default=42, type=int)
    parser.add_argument("-k", "--fs_per_label", default=4, type=int)
    parser.add_argument("-t", "--temperature", default=1.0, type=float)
    parser.add_argument("--save_dir", default="results/icl/sentiment_analysis/")
    parser.add_argument("--overwrite_cache", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    wandb.init(
        project="dialect-bench",
        group="sentiment_analysis",
        name=f"{args.lang}_{args.model}_k{args.fs_per_label}_t{args.temperature}_s{args.seed}",
        config=vars(args),
    )

    main(args)
