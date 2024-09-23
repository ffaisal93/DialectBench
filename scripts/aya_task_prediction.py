import random
from transformers import AutoTokenizer, AutoModelForCausalLM
from instructions import INSTRUCTIONS
from utils_prompt import PreambleCreator, PromptAdder, KShotExamplePreparer
from load_datasets import *
from utils_llm import *

import argparse
import os
import csv
import json
import random
from tqdm import tqdm
import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, Dataset, DatasetDict
from transformers import logging
import pickle
#datasets 2.4.0
#pandas 1.4.3






def main(args):
    def get_result_dict(result_file_path, task):
        # Check if the file exists
        if os.path.exists(result_file_path):
            # Load the dictionary from the pickle file
            with open(result_file_path, "rb") as file:
                results = pickle.load(file)
                print(f'result file loaded from: {result_file_path}')
        else:
            print(f'defining empty result file')
            results={}
        return results

    def generate_result(prompts,gen_config,model_name='aya',bs=4):
        all_response=[]
        all_response_raw=[]
        end=len(prompts)
        count=0
        for start in tqdm(range(0,end,bs)):
            count+=1
            stop=min(start+bs,len(prompts))
            if start<stop:
                prompts_batch=prompts[start:stop]
                encodings=tokenizer(prompts_batch, return_tensors="pt",  padding=True,truncation=True, max_length=3000).to("cuda")
                with torch.no_grad():
                    output_ids = model.generate(**encodings, **gen_config)
                    # Move the output_ids tensor to CPU
                    output_ids = output_ids.cpu()
                    responses=tokenizer.batch_decode(output_ids, skip_special_tokens=True)
                    all_response.extend(responses)
                # Clear the GPU memory used by sub_encodings
                    del encodings
                    torch.cuda.empty_cache()
                    
        return all_response

    def predict_sentiment():
        sa_datapath = 'data/sentiment_analysis/'
        metadata_filepath = 'metadata/sentiment_metadata.json'
        all_dataset = load_sa(sa_datapath, metadata_filepath)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        count=0
        #ar-lb rating system
        for lang in all_dataset:
            if lang not in results:
                results[lang]={}
            for variety in all_dataset[lang]:
                # if count>0:
                #     break
                count+=1
                if variety not in results[lang]:
                    variety_ds = all_dataset[lang][variety]
                    variety_ds = variety_ds.filter(lambda example: example["label"] is not None and example["label"] != 'label')
                    variety_ds_wprompt = variety_ds.map(PromptAdder.add_prompted_sa, fn_kwargs={"dataset": variety_ds}, batched=False, load_from_cache_file=False)
                    preamble = PreambleCreator.create_preamble_sa(variety_ds['train'])
                    shot = 3
                    kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, variety_ds_wprompt['train'], variety_ds_wprompt['test'], 'label', shot)
                    print(lang, variety)
                    print(kshot)
                    print(prompted_test_examples[0])
                    print(test_labels[0])

                    all_response=generate_result(prompted_test_examples,gen_config)
                    results[lang][variety]={
                        'response': all_response,
                        'true_labels': test_labels
                    }
                    print("---------------------------------------------------------\n")
                    print(all_response[:10])
                    print(test_labels[:10])

                    # Save the dictionary to the pickle file
                    with open(result_file_path, "wb") as file:
                        pickle.dump(results, file)


    def predict_nli():
        lang = 'all'
        metadata_filepath = 'metadata/nli_metadata.json'
        dataset_scriptpath = "scripts/nli/dialect_nli.py"
        all_dataset = load_nli(metadata_filepath, dataset_scriptpath, lang)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        count=0
        
        train_dataset = all_dataset['eng_Latn']['train'].shuffle(seed=42).select(range(2000))
        train_dataset = train_dataset.filter(lambda example: example["label"] is not None and example["label"] != 'label')
        train_dataset = train_dataset.map(PromptAdder.add_prompted_nli, fn_kwargs={"dataset": train_dataset}, batched=False, load_from_cache_file=False)
        preamble = PreambleCreator.create_preamble_nli(train_dataset)

        for lang in all_dataset:
            if lang not in results:
                variety_ds = all_dataset[lang]
                variety_ds = variety_ds.filter(lambda example: example["label"] is not None and example["label"] != 'label')
                variety_ds_wprompt = variety_ds.map(PromptAdder.add_prompted_nli, fn_kwargs={"dataset": variety_ds}, batched=False, load_from_cache_file=False)
                shot = 3
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, variety_ds_wprompt['test'], 'label_text', shot)
                print(lang)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=generate_result(prompted_test_examples,gen_config)
                results[lang]={
                    'response': all_response,
                    'true_labels': test_labels
                }
                print("---------------------------------------------------------\n")
                print(all_response[:10])
                print(test_labels[:10])

                # Save the dictionary to the pickle file
                with open(result_file_path, "wb") as file:
                    pickle.dump(results, file)


    def predict_sib():
        datapaths = 'data/topic_class'
        metadata_filepath = 'metadata/topic_metadata.json'
        all_dataset = load_sib(datapaths, metadata_filepath)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        zeroshot_lang='eng_Latn'
        zeroshot_train_dataset = all_dataset[zeroshot_lang]['train']
        zeroshot_train_dataset = zeroshot_train_dataset.filter(lambda example: example["label"] is not None)
        zeroshot_train_dataset = zeroshot_train_dataset.map(PromptAdder.add_prompted_sib, fn_kwargs={"dataset": zeroshot_train_dataset}, batched=False, load_from_cache_file=False)

        for lang in all_dataset:
            if lang not in results:
                if args.prompt_lang=='in_language' and 'train' in all_dataset[lang]:
                    train_dataset = all_dataset[lang]['train']
                    train_dataset = train_dataset.filter(lambda example: example["label"] is not None)
                    train_dataset = train_dataset.map(PromptAdder.add_prompted_sib, fn_kwargs={"dataset": train_dataset}, batched=False, load_from_cache_file=False)
                elif args.prompt_lang=='zeroshot':
                    train_dataset=zeroshot_train_dataset
                else:
                    continue
                
                preamble = PreambleCreator.create_preamble_sib(train_dataset)
                
                test_dataset = all_dataset[lang]['test']
                test_dataset = test_dataset.filter(lambda example: example["label"] is not None)
                test_dataset = test_dataset.map(PromptAdder.add_prompted_sib, fn_kwargs={"dataset": test_dataset}, batched=False, load_from_cache_file=False)
                
                # shot = 5
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label', shot)
                
                print(lang)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=generate_result(prompted_test_examples,gen_config)
                if len(all_response)==len(test_labels):
                    results[lang]={
                        'response': all_response,
                        'true_labels': test_labels
                    }
                    print("---------------------------------------------------------\n")
                    print(all_response[:10])
                    print(test_labels[:10])

                    # Save the dictionary to the pickle file
                    with open(result_file_path, "wb") as file:
                        pickle.dump(results, file)
                    print(f'{task} lang:{lang} results saved in {result_file_path}')
                else:
                    print(len(all_response),len(test_labels))
                    print(all_response[-10:])
                    print(test_labels[-10:])
                    print("mismatch true label count and response count")

    def predict_did():
        datapaths={'arabic':'data/dialect-identification/arabic/MADAR/MADAR_Corpus',
          'other':'data/dialect-identification'}
        all_dataset = load_did(datapaths)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)


        for lang in all_dataset:
            if lang not in results:
                train_dataset = all_dataset[lang]['train']
                train_dataset = train_dataset.filter(lambda example: example["label"] is not None)
                train_dataset = train_dataset.map(PromptAdder.add_prompted_did, fn_kwargs={"dataset": train_dataset}, batched=False, load_from_cache_file=False)
                
                preamble = PreambleCreator.create_preamble_did(train_dataset)
                print(preamble)
                
                if 'test' in all_dataset[lang].keys():
                    test_split='test'
                else:
                    test_split='dev'    
                test_dataset = all_dataset[lang][test_split]
                test_dataset = test_dataset.filter(lambda example: example["label"] is not None)
                test_dataset = test_dataset.map(PromptAdder.add_prompted_did, fn_kwargs={"dataset": test_dataset}, batched=False, load_from_cache_file=False)
                    
                shot = 1
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label', shot)
                    
                print(lang)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=generate_result(prompted_test_examples,gen_config)
                if len(all_response)==len(test_labels):
                    results[lang]={
                        'response': all_response,
                        'true_labels': test_labels
                    }
                    print("---------------------------------------------------------\n")
                    print(all_response[:10])
                    print(test_labels[:10])

                    # Save the dictionary to the pickle file
                    with open(result_file_path, "wb") as file:
                        pickle.dump(results, file)
                    print(f'{task} lang:{lang} results saved in {result_file_path}')
                else:
                    print(len(all_response),len(test_labels))
                    print(all_response[-10:])
                    print(test_labels[-10:])
                    print("mismatch true label count and response count")


    def predict_belebele():
        datapaths = 'data/reading-comprehension/Belebele'
        metadata_filepath = 'metadata/rcmc_metadata.json'
        all_dataset = load_belebele(datapaths, metadata_filepath)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        train_dataset = all_dataset['train'].shuffle(seed=42).select(range(2000))
        train_dataset = train_dataset.map(PromptAdder.add_prompted_belebele, fn_kwargs={"dataset": 'train'}, batched=False, load_from_cache_file=False)

        preamble = PreambleCreator.create_preamble_belebele(train_dataset)

        for lang in all_dataset['test']:
            if lang not in results:
                test_dataset = all_dataset['test'][lang]
                test_dataset = test_dataset.map(PromptAdder.add_prompted_belebele, fn_kwargs={"dataset": 'test'}, batched=False, load_from_cache_file=False)

                # shot = 3
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'correct_answer_num', shot)

                print(lang)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=generate_result(prompted_test_examples,gen_config)
                if len(all_response)==len(test_labels):
                    results[lang]={
                        'response': all_response,
                        'true_labels': test_labels
                    }
                    print("---------------------------------------------------------\n")
                    print(all_response[:10])
                    print(test_labels[:10])

                    # Save the dictionary to the pickle file
                    with open(result_file_path, "wb") as file:
                        pickle.dump(results, file)
                    print(f'{task} lang:{lang} results saved in {result_file_path}')
                else:
                    print(len(all_response),len(test_labels))
                    print(all_response[-10:])
                    print(test_labels[-10:])
                    print("mismatch true label count and response count")


    def predict_sdqa():
        datapaths = 'data/Question-Answering/SDQA-gold-task'
        all_dataset = load_sdqa(datapaths)
        langs = ["arabic", "bengali", "english", "korean", "swahili"]
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        if args.prompt_lang=='zeroshot':
            zeroshot_lang='english'
            zeroshot_train_dataset = all_dataset[zeroshot_lang]['train']
            zeroshot_train_dataset = zeroshot_train_dataset.map(PromptAdder.add_prompted_sdqa, batched=False, load_from_cache_file=False)
            train_dataset = zeroshot_train_dataset
        elif args.prompt_lang=='combined':
            combined_lang='all'
            combined_train_dataset = all_dataset[combined_lang]['train']
            combined_train_dataset = combined_train_dataset.map(PromptAdder.add_prompted_sdqa, batched=False, load_from_cache_file=False)
            train_dataset= combined_train_dataset
        preamble = PreambleCreator.create_preamble_sdqa()
        count=0

        for lang in langs:
            if lang not in results:
                results[lang]={}
                for variety in all_dataset:
                    if variety.startswith(lang) and variety != lang:
                        test_dataset = all_dataset[variety]['test']
                        test_dataset = test_dataset.map(PromptAdder.add_prompted_sdqa, batched=False, load_from_cache_file=False)
                        print(test_dataset[0])

                        # shot = 5
                        kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot, types='generative')

                        print(variety)
                        print(kshot)
                        print(prompted_test_examples[0])
                        print(test_labels[0])

                        all_response=generate_result(prompted_test_examples,gen_config)
                        if len(all_response)==len(test_labels):
                            results[lang][variety]={
                                'response': all_response,
                                'true_labels': test_labels
                            }
                            print("---------------------------------------------------------\n")
                            print(all_response[:10])
                            print(test_labels[:10])

                            # Save the dictionary to the pickle file
                            with open(result_file_path, "wb") as file:
                                pickle.dump(results, file)
                            print(f'{task} variety:{variety}, results saved in {result_file_path}')
                        else:
                            print(len(all_response),len(test_labels))
                            print(all_response[-10:])
                            print(test_labels[-10:])
                            print("mismatch true label count and response count")

    def predict_udp():
        metadata_filepath='metadata/udp_metadata.json'
        dataset_scriptpath="scripts/universal_dependencies.py"
        all_dataset=load_udp(metadata_filepath,dataset_scriptpath)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        
        zeroshot_lang='UD_English-EWT'
        zeroshot_train_dataset = all_dataset[zeroshot_lang]['train'].shuffle(seed=42).select(range(2000))
        zeroshot_train_dataset = zeroshot_train_dataset.map(PromptAdder.add_prompted_udp, batched=False, load_from_cache_file=False)

        preamble = PreambleCreator.create_preamble_udp()
        print(preamble)
        print(zeroshot_train_dataset['text'][0])
        print(zeroshot_train_dataset['label_text'][0])

        for variety in all_dataset:
            if variety not in results:
                if 'train' in all_dataset[variety]:
                    min_range=min(2000, len(all_dataset[variety]['train']))
                    train_dataset = all_dataset[variety]['train'].shuffle(seed=42).select(range(min_range))
                    train_dataset = train_dataset.map(PromptAdder.add_prompted_udp, batched=False, load_from_cache_file=False)
                else:
                    train_dataset=zeroshot_train_dataset
                test_dataset = all_dataset[variety]['test']
                test_dataset = test_dataset.map(PromptAdder.add_prompted_udp, batched=False, load_from_cache_file=False)
                print(test_dataset[0])

                # shot = 5
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot,types='generative')
                
                print(variety)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=generate_result(prompted_test_examples,gen_config)
                results[variety]={
                    'response': all_response,
                    'true_labels': test_labels
                }
                print("---------------------------------------------------------\n")
                print(all_response[:10])
                print(test_labels[:10])

                # Save the dictionary to the pickle file
                with open(result_file_path, "wb") as file:
                    pickle.dump(results, file)

    def predict_pos():
        metadata_filepath='metadata/pos_metadata.json'
        dataset_scriptpath="scripts/universal_dependencies.py"
        all_dataset=load_pos(metadata_filepath,dataset_scriptpath)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        zeroshot_lang='UD_English-EWT'
        zeroshot_train_dataset = all_dataset[zeroshot_lang]['train'].shuffle(seed=42).select(range(2000))
        zeroshot_train_dataset = zeroshot_train_dataset.map(PromptAdder.add_prompted_pos, batched=False, load_from_cache_file=False)

        preamble = PreambleCreator.create_preamble_pos()
        print(preamble)
        print(zeroshot_train_dataset['text'][0])
        print(zeroshot_train_dataset['label_text'][0])

        for variety in all_dataset:
            if variety not in results:
                if 'train' in all_dataset[variety]:
                    min_range=min(2000, len(all_dataset[variety]['train']))
                    train_dataset = all_dataset[variety]['train'].shuffle(seed=42).select(range(min_range))
                    train_dataset = train_dataset.map(PromptAdder.add_prompted_pos, batched=False, load_from_cache_file=False)
                else:
                    train_dataset=zeroshot_train_dataset
                test_dataset = all_dataset[variety]['test']
                test_dataset = test_dataset.map(PromptAdder.add_prompted_pos, batched=False, load_from_cache_file=False)
                print(test_dataset[0])

                # shot = 5
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot,types='generative')
                
                print(variety)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=generate_result(prompted_test_examples,gen_config)
                results[variety]={
                    'response': all_response,
                    'true_labels': test_labels
                }
                print("---------------------------------------------------------\n")
                print(all_response[:10])
                print(test_labels[:10])

                # Save the dictionary to the pickle file
                with open(result_file_path, "wb") as file:
                    pickle.dump(results, file)

    def predict_ner():
        metadata_filepath='metadata/ner_metadata.json'
        dataset_scriptpath="wikiann"
        all_dataset=load_ner(metadata_filepath,dataset_scriptpath)
        # Specify the file path for the pickle file
        result_file_path = os.path.join(result_path, f"{task}.pkl")
        results=get_result_dict(result_file_path, task)

        zeroshot_lang='en'
        zeroshot_train_dataset = all_dataset[zeroshot_lang]['train'].shuffle(seed=42).select(range(2000))
        zeroshot_train_dataset = zeroshot_train_dataset.map(PromptAdder.add_prompted_ner, batched=False, load_from_cache_file=False)

        preamble = PreambleCreator.create_preamble_ner()
        print(preamble)
        print(zeroshot_train_dataset['text'][0])
        print(zeroshot_train_dataset['label_text'][0])

        for variety in all_dataset:
            # if 'train' in all_dataset[variety]:
            #     min_range=min(2000, len(all_dataset[variety]['train']))
            #     train_dataset = all_dataset[variety]['train'].shuffle(seed=42).select(range(min_range))
            #     train_dataset = train_dataset.map(PromptAdder.add_prompted_pos, batched=False, load_from_cache_file=False)
            # else:
            #     train_dataset=zeroshot_train_dataset
            if variety not in results and len(all_dataset[variety]['test'])!=0:
                train_dataset=zeroshot_train_dataset
                test_dataset = all_dataset[variety]['test']
                test_dataset = test_dataset.map(PromptAdder.add_prompted_ner, batched=False, load_from_cache_file=False)
                print(test_dataset[0])

                # shot = 5
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot,types='generative')
                
                print(variety)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=generate_result(prompted_test_examples,gen_config)
                results[variety]={
                    'response': all_response,
                    'true_labels': test_labels
                }
                print("---------------------------------------------------------\n")
                print(all_response[:10])
                print(test_labels[:10])

                # Save the dictionary to the pickle file
                with open(result_file_path, "wb") as file:
                    pickle.dump(results, file)


    # load base LLM model and tokenizer
    model_name="/projects/antonis/models/aya-101"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir='/scratch/ffaisal/cache/models',  load_in_8bit=True, device_map={"":0})
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    max_token=5
    if args.task in ['udp','pos','ner']:
    	max_token=500
    elif args.task in ['sdqa']:
    	max_token=15
    gen_config = {
                "temperature": 0.7,
                "top_p": 0.1,
                "repetition_penalty": 1.18,
                "top_k": 5,
                "do_sample": True,
                "max_new_tokens": max_token,
                "pad_token_id": tokenizer.eos_token_id
                    }
    print(gen_config)
    tokenizer.pad_token_id = tokenizer.eos_token_id

    # Specify the directory path
    result_path = f"./llm_results/{args.model}/{args.prompt_lang}"

    # Create the directory if it doesn't exist
    if not os.path.exists(result_path):
        os.makedirs(result_path)


    ##=======================================================================================
    task=args.task
    # Assuming you have parsed the command-line arguments and stored the task in `args.task`
    shot=args.shot
    if task == 'sentiment':
        predict_sentiment()
    elif task == 'nli':
        predict_nli()
    elif task == 'topic':
        predict_sib()
    elif task == 'belebele':
        predict_belebele()
    elif task == 'sdqa':
        predict_sdqa()
    elif task == 'udp':
        predict_udp()
    elif task == 'pos':
        predict_pos()
    elif task == 'ner':
        predict_ner()
    elif task == 'did':
        predict_did()
    else:
        print("Invalid task argument.")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, required=True, help='Task to perform')
    parser.add_argument('--shot', type=int, default=3, help='How many examples in each prompt')
    parser.add_argument('--model', type=str, default="gpt-35", help='How many examples in each prompt')
    parser.add_argument('--prompt_lang', type=str, default="zeroshot", help='the prompt lang is either zeroshot, in_cluster or in_language')
    args = parser.parse_args()
    print(args)
    main(args)
    # predict_sentiment()
    # predict_nli()
    # predict_sib()
    # predict_belebele()
    # predict_sdqa()
    # predict_udp()
    # predict_pos()
    # predict_ner()
