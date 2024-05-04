import pandas as pd
import json
from datasets import load_dataset, load_from_disk, DatasetDict, Dataset
import os
from collections import defaultdict


import subprocess
import sys
import importlib
from packaging import version



def load_metadata(filepath):
    f = open(filepath)
    metadata = json.load(f)
    # Closing file
    f.close()
    return metadata


def load_udp(metadata_filepath,
             dataset_scriptpath,
             lang='all',
             CACHE_DIR='.cache'):
    metadata=load_metadata(metadata_filepath)
    all_lang=pd.DataFrame(metadata).T
    all_dataset={}
    if lang=='all':
        for ulang in list(all_lang.index):
            dataset = load_dataset(dataset_scriptpath, ulang,
                    cache_dir=CACHE_DIR)
            all_dataset[ulang]=dataset
        all_dataset=DatasetDict(all_dataset)
    else:
        all_dataset[lang] = load_dataset(dataset_scriptpath, lang,
                    cache_dir=CACHE_DIR)
        all_dataset=DatasetDict(all_dataset)
    return all_dataset

def load_pos(metadata_filepath,
             dataset_scriptpath,
             lang='all',
             CACHE_DIR='.cache',
             data_dir="data/pos_tagging"):
    metadata=load_metadata(metadata_filepath)
    all_lang=pd.DataFrame(metadata).T
    all_dataset={}
    if lang=='all':
        dataset_scripts={
            "ud":"scripts/universal_dependencies.py",
            "noisy":"scripts/pos_tagging/noisy_dialect.py"
            }
        ud_ones=all_lang[all_lang['dataset']=='ud']
        for ulang in list(ud_ones.index):
            dataset = load_dataset(dataset_scripts['ud'], ulang,
                    cache_dir=CACHE_DIR)
            all_dataset[ulang]=dataset
        noisy_ones=all_lang[all_lang['dataset']=='noisy']
        for nlang in noisy_ones.index:
            dataset = load_dataset(dataset_scripts['noisy'], nlang,
                data_dir=data_dir,
                    cache_dir=CACHE_DIR)
            all_dataset[ulang]=dataset
        all_dataset=DatasetDict(all_dataset)
    else:
        all_dataset[lang] = load_dataset(dataset_scriptpath, lang,
                    cache_dir=CACHE_DIR)
        all_dataset=DatasetDict(all_dataset)
    return all_dataset

def load_ner(metadata_filepath,
             dataset_scriptpath,
             lang='all',
             CACHE_DIR='.cache/ner'):
    metadata=load_metadata(metadata_filepath)
    all_lang=pd.DataFrame(metadata).T
    all_dataset={}
    if lang=='all':
        dataset_scripts={
            "wikiann":"wikiann",
            "wikiann_og":"scripts/ner/wikiann_og.py",
            "norwegian_ner":"scripts/ner/norwegian_ner.py"
            }
        
        ud_ones=all_lang[(all_lang['huggingface']==True) & (all_lang['dataset']=='wikiann')]
        for ulang in list(ud_ones.index):
            dataset = load_dataset(dataset_scripts['wikiann'], ulang,
                    cache_dir=CACHE_DIR)
            all_dataset[ulang]=dataset
        
        ud_ones=all_lang[(all_lang['huggingface']==False) & (all_lang['dataset']=='wikiann')]
        for ulang in list(ud_ones.index):
            dataset = load_dataset(dataset_scripts['wikiann_og'], ulang,
                    cache_dir=CACHE_DIR)
            all_dataset[ulang]=dataset
        
        #norwegian_ner::discarded
        # ud_ones=all_lang[(all_lang['huggingface']==True) & (all_lang['dataset']=='norwegian_ner')]
        # for ulang in list(ud_ones.index)[:3]:
        #     dataset = load_dataset(dataset_scripts['norwegian_ner'], ulang,
        #             cache_dir=CACHE_DIR)
        #     all_dataset[ulang]=dataset
            
        all_dataset=DatasetDict(all_dataset)
    else:
        all_dataset[lang] = load_dataset(dataset_scriptpath, lang,
                    cache_dir=CACHE_DIR)
        all_dataset=DatasetDict(all_dataset)
    return all_dataset
    

def load_did(datapaths):
    count_lang=0
    arabic='data/dialect-identification/arabic/MADAR/MADAR_Corpus'

    all_dataset={}
    all_dataset['arabic']={}
    for f in ['train.csv','dev.csv','test.csv']:
        all_dataset['arabic'][f.split('.')[0]]=Dataset.from_pandas(pd.read_csv(os.path.join(datapaths['arabic'],f)))
    

    for f in os.listdir(datapaths['other']):
        if f!='arabic' and not str(f).startswith('.'):
            all_dataset[f]={}
            for f1 in os.listdir(os.path.join(datapaths['other'],f)):
                if str(f1) in ['train.csv','dev.csv','test.csv']:
                    all_dataset[f][str(f1).split('.')[0]]=Dataset.from_pandas(pd.read_csv(os.path.join(datapaths['other'],f,f1)))
    all_dataset=DatasetDict(all_dataset)
    return all_dataset

def load_sdqa(datapaths):
    all_data={}
    for f in os.listdir(datapaths):
        split=str(f).split('-')[1]
        langname=str(f).replace('sdqa-','').replace('train-','').replace('test-','').replace('dev-','').replace('.json','')
    #     print(f,langname,split)
        if langname not in all_data:
            all_data[langname]={}
        all_data[langname][split]=load_dataset('json', data_files=os.path.join(datapaths,f),field='data')['train']
        all_data[langname]=DatasetDict(all_data[langname])
    all_data=DatasetDict(all_data)
    return all_data


def load_belebele(datapaths,metadata_filepath):
    metadata=load_metadata(metadata_filepath)
    all_lang=pd.DataFrame(metadata).T
    all_dataset={'test':{}}
    for lang in all_lang['code']:
        all_dataset['test'][lang]=load_dataset("json", data_files=f'{datapaths}/{lang}.jsonl')['train']
    all_dataset['train']=load_dataset("json", data_files=f'{datapaths}/train.jsonl')['train']
    all_dataset=DatasetDict(all_dataset)
    return all_dataset

def load_sib(datapaths,metadata_filepath):
    metadata=load_metadata(metadata_filepath)
    all_lang=pd.DataFrame(metadata).T
    all_dataset={}
    for lang in all_lang['code']:
        all_dataset[lang]={}
        for split in ['train','test','dev']:
            all_dataset[lang][split]=Dataset.from_pandas(pd.read_csv(f'{datapaths}/{lang}/{split}.csv'))
    all_dataset=DatasetDict(all_dataset)
    return all_dataset

def load_nli(metadata_filepath,
             dataset_scriptpath,
             lang='all',
             CACHE_DIR='.cache'):
    metadata=load_metadata(metadata_filepath)
    all_lang=pd.DataFrame(metadata).T
    all_dataset={}
    if lang=='all':
        for ulang in all_lang['code']:
            all_dataset[ulang]=load_dataset(dataset_scriptpath, ulang, cache_dir=CACHE_DIR)
    else:
        all_dataset[lang]=load_dataset(dataset_scriptpath, lang, cache_dir=CACHE_DIR)
    all_dataset=DatasetDict(all_dataset)
    return all_dataset

def load_sa(datapaths, metadata_filepath):
    metadata=load_metadata(metadata_filepath)
    all_lang=pd.DataFrame(metadata).T
    print(metadata)
    all_dataset={}
    for grp,f in all_lang.groupby('langgroup'):
        all_dataset[grp]={}
        for lang,df in f.iterrows():
            all_dataset[grp][lang]={}
            for split in ['train','validation','test']:
                all_dataset[grp][lang][split] = load_dataset(
                        "csv",
                        data_files=f'{datapaths}/{grp}/{lang}/{split}.csv',on_bad_lines='skip')['train']
            all_dataset[grp][lang]=DatasetDict(all_dataset[grp][lang])
    all_dataset=DatasetDict(all_dataset)
    return all_dataset