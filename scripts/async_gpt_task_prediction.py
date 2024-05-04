import random
from transformers import AutoTokenizer, AutoModelForCausalLM
from instructions import INSTRUCTIONS
from utils_prompt import PreambleCreator, PromptAdder, KShotExamplePreparer
from load_datasets import *
from utils_llm import *
import openai

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
import subprocess
import sys
import asyncio
from tqdm.asyncio import tqdm

def main(args):
    # Text completion using GPT
    def trim_text(text):
        return text.strip().strip('\n').strip('\\n')

    def generate_using_gpt(prompt):
        choices = [""] * len(prompt)
        try:
            # Create a completion for the provided prompt and parameters
            # To know more about the parameters, checkout this documentation: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference
            response = client.completions.create(
                model=deployment_name,
                prompt=prompt, 
                max_tokens=max_token,
                temperature=0,
                top_p=1,
                stop=None,
                frequency_penalty=0,
                presence_penalty=0.0)
            
            choices = [choice.text.strip() for choice in response.choices]

        except openai.APITimeoutError as e:
            # Handle request timeout
            print(f"Request timed out: {e}")
        
        except openai.AuthenticationError as e:
            # Handle Authentication error here, e.g. invalid API key
            print(f"OpenAI API returned an Authentication Error: {e}")

        except openai.APIConnectionError as e:
            # Handle connection error here
            print(f"Failed to connect to OpenAI API: {e}")

        except openai.BadRequestError as e:
            # Handle connection error here
            print(f"Invalid Request Error: {e}")

        except openai.BadRequestError as e:
            # Handle connection error here
            print(f"Invalid Request Error: {e}")
            
        except openai.RateLimitError as e:
            # Handle rate limit error
            print(f"OpenAI API request exceeded rate limit: {e}")

        except openai.InternalServerError as e:
            # Handle Service Unavailable error
            print(f"Service Unavailable: {e}")

        except openai.APIError as e:
            # Handle API error here, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
        except Exception as e:
            # Handle API errors for individual prompts
            print(f"OpenAI API returned an Error (first round)")
            print(f"Error: {e}")

        # Iterate over the prompts and send individual requests for failed prompts
        for i, choice in enumerate(choices):
            if choice == "":
                try:
                    response = client.completions.create(
                        model=deployment_name,
                        prompt=prompt[i],
                        max_tokens=max_token,
                        temperature=0,
                        top_p=1,
                        stop=None,
                        frequency_penalty=0,
                        presence_penalty=0.0)
                    choices[i] = response.choices[0].text.strip()
                except Exception as e:
                    # Handle API errors for individual prompts
                    print(f"OpenAI API returned an Error for prompt: {prompt[i]}")
                    print(f"Error: {e}")
                    # Leave the default value ("") for this prompt
        return choices


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


    def prepare_send_get_batch(prompted_test_examples, batch_size=5):
        predictions = []
        
        # Calculate the number of batches
        num_batches = len(prompted_test_examples) // batch_size
        if len(prompted_test_examples) % batch_size != 0:
            num_batches += 1
        
        # Create a progress bar using tqdm
        progress_bar = tqdm(total=len(prompted_test_examples), unit='prompt')
        
        # Iterate over the batches
        for i in range(num_batches):
            start_index = i * batch_size
            end_index = min((i + 1) * batch_size, len(prompted_test_examples))
            
            # Get the current batch of prompts
            prompt_batch = prompted_test_examples[start_index:end_index]
            
            # if i==31:   
            # Send the batch to the generate_using_gpt function
            batch_predictions = asyncio.run(call_all_prompt(prompt_batch))
            
            # Extend the main prediction list with the batch predictions
            predictions.extend(batch_predictions)
                
            # Update the progress bar
            progress_bar.update(len(prompt_batch))
        
        # Close the progress bar
        progress_bar.close()
        
        return predictions

    async def create_chat_completion(messages):
        while True:
            try:
                chat_completion = await client.chat.completions.create(
                    model=deployment_name,
                    messages=messages,
                    max_tokens=max_token,
                    temperature=0,
                    top_p=1,
                    stop=None,
                    frequency_penalty=0,
                    presence_penalty=0.0,
                )
                return chat_completion.choices[0].message.content
            except Exception as e:
                print(f"Chat completion request failed: {str(e)}")
                if "429" in str(e):
                    print("Rate limit exceeded. Retrying in 10 seconds...")
                    await asyncio.sleep(3)
                else:
                    return ""

    async def call_all_prompt(list_of_messages):
        tasks = []
        for messages in list_of_messages:
            task = asyncio.create_task(create_chat_completion(messages))
            tasks.append(task)

        completions = await asyncio.gather(*tasks)
        # completions = []
        # for task in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Chat Completions"):
        #     completion = await task
        #     completions.append(completion)


        # response_contents = []
        # for completion in completions:
        #     if completion is not None:
        #         response_contents.append(completions)
        #     else:
        #         response_contents.append(None)

        return completions

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
                    # shot = 3
                    kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, variety_ds_wprompt['train'], variety_ds_wprompt['test'], 'label', shot)
                    print(lang, variety)
                    print(kshot)
                    print(prompted_test_examples[0])
                    print(test_labels[0])
                    prompted_test_examples=KShotExamplePreparer.prepare_chat_completion_prompts(prompted_test_examples, task)
                    print(prompted_test_examples[0])

                    # all_response = asyncio.run(call_all_prompt(prompted_test_examples))
                    all_response=prepare_send_get_batch(prompted_test_examples)

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
                    else:
                        print(len(all_response),len(test_labels))
                        print(all_response[-10:])
                        print(test_labels[-10:])
                        print("mismatch true label count and response count")


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
                # if count>0:
                #     break
                count+=1
                variety_ds = all_dataset[lang]
                variety_ds = variety_ds.filter(lambda example: example["label"] is not None and example["label"] != 'label')
                variety_ds_wprompt = variety_ds.map(PromptAdder.add_prompted_nli, fn_kwargs={"dataset": variety_ds}, batched=False, load_from_cache_file=False)
                # shot = 3
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, variety_ds_wprompt['test'], 'label_text', shot)
                print(lang)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])
                prompted_test_examples=KShotExamplePreparer.prepare_chat_completion_prompts(prompted_test_examples, task)

                all_response=prepare_send_get_batch(prompted_test_examples)
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
                else:
                    print(len(all_response),len(test_labels))
                    print(all_response[-10:])
                    print(test_labels[-10:])
                    print("mismatch true label count and response count")


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
        count=0
        for lang in all_dataset:
            if lang not in results:
                # if count>0:
                #     break
                count+=1
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
                prompted_test_examples=KShotExamplePreparer.prepare_chat_completion_prompts(prompted_test_examples, 'sib')

                all_response=prepare_send_get_batch(prompted_test_examples)

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
                    print('{task} lang:{lang} results saved in {result_file_path}')
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
        count=0
        for lang in all_dataset['test']:
            if lang not in results:
                # if count>0:
                #     break
                count+=1
                test_dataset = all_dataset['test'][lang]
                test_dataset = test_dataset.map(PromptAdder.add_prompted_belebele, fn_kwargs={"dataset": 'test'}, batched=False, load_from_cache_file=False)

                # # shot = 3
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'correct_answer_num', shot)

                print(lang)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                prompted_test_examples=KShotExamplePreparer.prepare_chat_completion_prompts(prompted_test_examples, task)
                print(prompted_test_examples[0])
                all_response=prepare_send_get_batch(prompted_test_examples)

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
                    print('{task} lang:{lang} results saved in {result_file_path}')
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
                        # if count>0:
                        #     break
                        count+=1
                        test_dataset = all_dataset[variety]['test']
                        test_dataset = test_dataset.map(PromptAdder.add_prompted_sdqa, batched=False, load_from_cache_file=False)
                        print(test_dataset[0])

                        # shot = 5
                        kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot, types='generative')

                        print(variety)
                        print(kshot)
                        print(prompted_test_examples[0])
                        print(test_labels[0])

                        prompted_test_examples=KShotExamplePreparer.prepare_chat_completion_prompts(prompted_test_examples, task)
                        print(prompted_test_examples[0])
                        all_response=prepare_send_get_batch(prompted_test_examples)

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
                            print('{task} variety:{variety}, results saved in {result_file_path}')
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
                if args.prompt_lang=='in_language' and 'train' in all_dataset[variety]:
                    min_range=min(2000, len(all_dataset[variety]['train']))
                    train_dataset = all_dataset[variety]['train'].shuffle(seed=42).select(range(min_range))
                    train_dataset = train_dataset.map(PromptAdder.add_prompted_udp, batched=False, load_from_cache_file=False)
                elif args.prompt_lang=='zeroshot':
                    train_dataset=zeroshot_train_dataset
                else:
                    continue
                test_dataset = all_dataset[variety]['test']
                test_dataset = test_dataset.map(PromptAdder.add_prompted_udp, batched=False, load_from_cache_file=False)
                print(test_dataset[0])

                # shot = 5
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot,types='generative')
                
                print(variety)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=prepare_send_get_batch(prompted_test_examples)
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
                if args.prompt_lang=='in_language' and 'train' in all_dataset[variety]:
                    min_range=min(2000, len(all_dataset[variety]['train']))
                    train_dataset = all_dataset[variety]['train'].shuffle(seed=42).select(range(min_range))
                    train_dataset = train_dataset.map(PromptAdder.add_prompted_pos, batched=False, load_from_cache_file=False)
                elif args.prompt_lang=='zeroshot':
                    train_dataset=zeroshot_train_dataset
                else:
                    continue
                test_dataset = all_dataset[variety]['test']
                test_dataset = test_dataset.map(PromptAdder.add_prompted_pos, batched=False, load_from_cache_file=False)
                print(test_dataset[0])

                # shot = 5
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot,types='generative')
                
                print(variety)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=prepare_send_get_batch(prompted_test_examples)
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
            if variety not in results:
                if args.prompt_lang=='in_language' and 'train' in all_dataset[variety]:
                    continue
                elif args.prompt_lang=='zeroshot':
                    train_dataset=zeroshot_train_dataset
                else:
                    continue
                test_dataset = all_dataset[variety]['test']
                test_dataset = test_dataset.map(PromptAdder.add_prompted_ner, batched=False, load_from_cache_file=False)
                print(test_dataset[0])

                # shot = 5
                kshot, prompted_test_examples, test_labels = KShotExamplePreparer.prepare_kshot(preamble, train_dataset, test_dataset, 'label_text', shot,types='generative')
                
                print(variety)
                print(kshot)
                print(prompted_test_examples[0])
                print(test_labels[0])

                all_response=prepare_send_get_batch(prompted_test_examples)
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


    # Currently OPENAI API have the following versions available: https://learn.microsoft.com/azure/ai-services/openai/reference
    api_version = "2023-09-15-preview"

    base='delphi'
    base='dbench'

    if base=='delphi':
        # Setting up the deployment name
        deployment_name = "gpt-35-turbo-instruct"

        # The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
        # This is the value of the endpoint for your Azure OpenAI resource
        azure_endpoint = "https://delphi.openai.azure.com/"

        # The API key for your Azure OpenAI resource.
        api_key = "33847c64a3264c1b930a4f8e18cfc6b5"

    elif base=='olimpia':
        # Setting up the deployment name
        deployment_name = "gpt-35-turbo"

        # The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
        # This is the value of the endpoint for your Azure OpenAI resource
        azure_endpoint = "https://olympia.openai.azure.com/"

        # The API key for your Azure OpenAI resource.
        api_key = "91c6b13def6e4e1bb6adecd6a4a0999b"

    elif base=='dbench':
        api_version = "2024-02-15-preview"
        # Setting up the deployment name
        deployment_name = "dbench"

        # The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
        # This is the value of the endpoint for your Azure OpenAI resource
        azure_endpoint = "https://dbench.openai.azure.com/"

        # The API key for your Azure OpenAI resource.
        api_key = "cbd70e1045114317b6187f2df308bf0b"
        
    client = openai.AsyncAzureOpenAI(
          api_key=api_key,  
          azure_endpoint=azure_endpoint,
          api_version=api_version
        )


    max_token=5
    if args.task in ['udp','pos','ner']:
        max_token=500
    elif args.task in ['sdqa']:
        max_token=15


    # Specify the directory path
    result_path = f"./llm_results/{args.model}/{args.prompt_lang}"

    # Create the directory if it doesn't exist
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    task=args.task
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
    else:
        print("Invalid task argument.")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, required=True, help='Task to perform')
    parser.add_argument('--shot', type=int, default=3, help='How many examples in each prompt')
    parser.add_argument('--model', type=str, default="gpt-35", help='How many examples in each prompt')
    parser.add_argument('--prompt_lang', type=str, default="zeroshot", help='the prompt lang is either zeroshot, in_cluster or in_language')
    args = parser.parse_args()
    main(args)
    # predict_sentiment()
    # predict_nli()
    # predict_sib()
    # predict_belebele()
    # predict_sdqa()
    # predict_udp()
    # predict_pos()
    # predict_ner()
