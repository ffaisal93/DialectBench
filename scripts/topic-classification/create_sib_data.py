import pandas as pd
import os

"""
taken and adapted from https://github.com/dadelani/sib-200/tree/main

@misc{adelani2023sib200,
      title={SIB-200: A Simple, Inclusive, and Big Evaluation Dataset for Topic Classification in 200+ Languages and Dialects}, 
      author={David Ifeoluwa Adelani and Hannah Liu and Xiaoyu Shen and Nikita Vassilyev and Jesujoba O. Alabi and Yanke Mao and Haonan Gao and Annie En-Shiun Lee},
      year={2023},
      eprint={2309.07445},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""

def read_text(filenam):
    with open(filenam) as f:
        text_lines = f.read().splitlines()

    return text_lines


def create_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def get_dict_index_text(df):
    dict_title_text = {}
    N_samples = df.shape[0]
    for i in range(N_samples):
        dict_title_text[df['index_id'].iloc[i]] = df['text'].iloc[i]

    return dict_title_text

#lang = 'kik_Latn'

list_langs = set([lang.split('.')[0] for lang in os.listdir('data/raw/')])

for lang in list_langs:
    print(lang)
    dev = read_text('data/raw/'+lang+'.dev')
    devtest = read_text('data/raw/'+lang+'.devtest')

    #print(len(dev), len(devtest))

    all_texts = dev + devtest

    df_all = pd.DataFrame(all_texts, columns=['text'])

    df_all['index_id'] = list(range(df_all.shape[0]))

    dict_index_text = get_dict_index_text(df_all)

    output_dir = 'data/topic_class/'+lang+'/'
    create_dir(output_dir)

    for split in ['train', 'dev', 'test']:
        df = pd.read_csv('sib-200/data/eng/'+split+'.tsv', sep='\t')

        df['lang_text'] = df['index_id'].map(dict_index_text)
        df['lang_text'] = df['lang_text'].str.rstrip()
        df.columns = ['index_id', 'category', 'source_text', 'text']
        df.rename(columns={"text": "sentence", "category": "label"},inplace=True)

        df[['index_id', 'label', 'sentence']].to_csv(output_dir+split+'.csv', index=None)

    labels = read_text('sib-200/data/eng/labels.txt')
    with open(output_dir+'labels.txt', 'w') as f:
        for l in labels:
            f.write(l+'\n')


