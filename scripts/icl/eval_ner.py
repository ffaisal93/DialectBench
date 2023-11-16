import argparse
import os
import csv
import json
from collections import Counter
import random
from tqdm import tqdm
import wandb
import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset, Dataset, DatasetDict
from evaluate import load
from transformers import logging

logging.set_verbosity_error()

CACHE_DIR = "/gscratch/argon/kahuja/.cache/"
DATA_DIR = "data/NER"

METADATA = json.load(open("metadata/ner_metadata.json"))

WIKIANN_TAGS = [
    "O",
    "B-PER",
    "I-PER",
    "B-ORG",
    "I-ORG",
    "B-LOC",
    "I-LOC",
]

NORNER_TAGS = [
    "O",
    "B-OTH",
    "I-OTH",
    "E-OTH",
    "S-OTH",
    "B-ORG",
    "I-ORG",
    "E-ORG",
    "S-ORG",
    "B-PRS",
    "I-PRS",
    "E-PRS",
    "S-PRS",
    "B-GEO",
    "I-GEO",
    "E-GEO",
    "S-GEO",
]

metric = load("seqeval")


def load_datasets(lang):
    dataset = METADATA[lang]["dataset"]
    huggingface = METADATA[lang]["huggingface"]

    script = "wikiann" if dataset == "wikiann" else "scripts/ner/norwegian_ner.py"
    if not huggingface:
        script = "scripts/ner/wikiann_og.py"

    datasets = load_dataset(script, lang, cache_dir=CACHE_DIR)

    # convert ner tag ids to tags
    if dataset == "wikiann":
        datasets = datasets.map(
            lambda example: {
                "ner_tags": [WIKIANN_TAGS[i] for i in example["ner_tags"]],
            },
            batched=True,
        )
    else:
        datasets = datasets.map(
            lambda example: {
                "ner_tags": [NORNER_TAGS[i] for i in example["ner_tags"]],
            },
            batched=True,
        )
    return datasets


def get_few_shot_examples(dataset, k=2, seed=42):
    few_shot_examples = []
    visited = []
    tag_counts = Counter()
    while True:
        example = random.choice(dataset)
        # Reject samples with no named entities'
        if len(set(example["ner_tags"])) == 1 and example["ner_tags"][0] == "O":
            continue
        # Reject samples with duplicate sentences
        if " ".join(example["tokens"]) in visited:
            continue
        few_shot_examples.append(example)
        visited.append(" ".join(example["tokens"]))

        # Update counter
        tag_counts.update(example["ner_tags"])

        # Check if all tags have at least k count
        if all([tag_counts[tag] >= k for tag in tag_counts]):
            break

    # shuffled = dataset.shuffle(seed=seed)
    # shuffled = shuffled.select(range(min(k, len(shuffled))))
    # few_shot_examples += [example for example in shuffled]
    return few_shot_examples


def construct_prompt(test_example, fs_example, wikiann=True):
    def example_to_prompt(example, add_label=True):
        ex_prompt = f"Input: {' '.join(example['tokens'])}\n"
        if add_label:
            # For token (tag) sequence
            output = " ".join(
                [
                    f"{token} ({tag})"
                    for token, tag in zip(example["tokens"], example["ner_tags"])
                ]
            )
            ex_prompt += f"Output: {output}\n"
        return ex_prompt

    if wikiann:
        instruction = "Given the following sentence, indicate the name entities (i.e., the real-world objects such as a person, location, organization, etc. that can be denoted with a proper name) such as 'New York Times'.  For each words of a named-entity, indicate their type 'LOC' or 'ORG' or 'PER', where 'LOC' indicates a location entity (such as 'New York City', 'ORG' indicates the token of an organization (such as 'Amazon'), 'PER' indicates the tokens of a person entity (such as 'Jeff Bezos'). To indicate boundaries of an entity, use IOB (Inside-Output-Begin) prefixes. The B- prefix before a tag indicates that the word is the beginning of a named entity. The I- prefix indicates that the word is inside a bigger chunk. For example, you can break 'New York' to 'New' and 'York.' and tag them as 'B-LOC' and 'I-LOC'. Any token that doesn't belong to a named entity must be tagged with 'O'."
    else:
        instruction = "Given the following Norwegian sentence, indicate the name entities (i.e., the real-world objects such as a person, location, organization, etc. that can be denoted with a proper name) such as 'New York Times'. For each words of a named-entity, indicate their type  'GEO' or 'ORG' or 'PRS', where 'GEO' indicates a location entity (such as 'New York City', 'ORG' indicates the token of an organization (such as 'Amazon'), 'PRS' indicates the tokens of a person entity (such as 'Jeff Bezos'). Named entities with other types should be indicated with 'OTH'. To indicate boundaries of an entity, use IOEBS (Inside-Output-End-Begin-Single) prefixes. The B- prefix before a tag indicates that the word is the beginning of a named entity. The I- prefix indicates that the word is inside a bigger chunk. The E- prefix indicates that the word is the end of a named entity. The S- prefix indicates that the word is a single-word entity. For example, you can break New York City to 'New', 'York', and 'City' and tag them as 'B-GEO', 'I-GEO', and 'E-GEO', while single toke entities like 'Paris' can be tagged as 'S-GEO'. Any token that doesn't belong to a named entity must be tagged with 'O'."

    prompt = instruction
    for example in fs_example:
        prompt += "\n\n" + example_to_prompt(example, add_label=True)

    prompt += "\n\n" + example_to_prompt(test_example, add_label=False)
    return prompt


def process_generation(text):
    generation_clean = text.split("\n\n")[0].strip().lower()
    # Recover tags from generation
    generated_tags = []
    for token in generation_clean.split():
        if token.startswith("("):
            tag = token.split("(")[1].split(")")[0]
            generated_tags.append(tag)
    return generated_tags


def evaluate_predictions(predictions, references):
    return metric.compute(predictions=predictions, references=references)


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


def evaluate_model(model, tokenizer, test_prompts, device):
    predictions = []
    references = []
    f1s, precisions, recalls = [], [], []
    for test_prompt in tqdm(test_prompts):
        # Generate
        generated_text = generate(
            model,
            tokenizer,
            test_prompt,
            device,
            max_tokens=20,
            temperature=1.0,
        )
        # Process
        generated_tags = process_generation(generated_text)
        predictions.append(generated_tags)
        references.append(test_prompt["ner_tags"])
        results = evaluate_predictions(predictions, references)
        f1, precision, recall = (
            results["overall_f1"],
            results["overall_precision"],
            results["overall_recall"],
        )
        f1s.append(f1)
        precisions.append(precision)
        recalls.append(recall)

    final_results = {
        "f1": f1s[-1],
        "precision": precisions[-1],
        "recall": recalls[-1],
    }

    return evaluate_predictions(predictions, references)
