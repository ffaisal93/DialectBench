import csv
import os
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from datasets import load_dataset

dataset = load_dataset("statworx/swiss-dialects")

def process_madar(datapath):
	datafiles=[]
	for f in os.listdir(datapath):
	    if str(f).startswith('MADAR') and 'index' not in str(f):
	        datafiles.append(os.path.join(datapath,f))

	train_df=pd.DataFrame()
	dev_df=pd.DataFrame()
	test_df=pd.DataFrame()
	for file in datafiles:
	    df=pd.read_csv(file,delimiter='\t')
	    df.rename(columns={"sent": "sentence", "lang": "label"},inplace=True)      
	    df_train=df[df['split'].str.contains('corpus-26-train')]
	    df_dev=df[df['split'].str.contains('corpus-26-dev')]
	    df_test=df[df['split'].str.contains('corpus-26-test')]
	    print(file, len(df_train), len(df_test), len(df_dev))
	    
	    train_df=pd.concat([train_df,df_train],axis=0)
	    dev_df=pd.concat([test_df,df_dev],axis=0)
	    test_df=pd.concat([test_df,df_test],axis=0)
	train_df=train_df.sample(frac=1).reset_index(drop=True)
	dev_df=dev_df.sample(frac=1).reset_index(drop=True)
	test_df=test_df.sample(frac=1).reset_index(drop=True)
	print('train:{}\ntest:{}\ndev:{}\n'.format(len(train_df),len(test_df),len(dev_df)))
	##save to csv
	train_df.to_csv(os.path.join(datapath,'train.csv'),index=False)
	dev_df.to_csv(os.path.join(datapath,'dev.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'test.csv'),index=False)

def process_tasc(dataset,datapath):
	files = ['test_neg.txt',
	'test_pos.txt', 'train_neg.txt', 'train_pos.txt']
	all_data={}
	for file in files:
		data = open(os.path.join(dataset,file)).read()
		# split=file[:-4].split('_')[0]
		label=file[:-4].split('_')[1]
		rows=[row for row in data.split('\n')]
		all_data[file[:-4]]=pd.DataFrame(rows,columns=['sentence'])
		all_data[file[:-4]]['label']=label
	train_df=pd.concat([all_data['train_neg'],all_data['train_pos']])
	train_df=train_df.sample(frac=1).reset_index(drop=True)
	test_df=pd.concat([all_data['test_neg'],all_data['test_pos']])
	test_df=test_df.sample(frac=1).reset_index(drop=True)

	# Dictionary mapping category -> new value                    
	mapping = {'pos': 'positive', 'neg': 'negative'}

	# Replace values where category matches mapping keys
	train_df['label'] = train_df['label'].sample(frac=1).map(mapping).fillna(train_df['label'])
	test_df['label'] = test_df['label'].sample(frac=1).map(mapping).fillna(test_df['label'])

	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'aeb_Arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'aeb_Arab-test.csv'),index=False)

def process_tunizi(dataset,datapath):
	files = ['TUNIZI_V2.txt']
	all_data={}
	for file in files:
		data = open(os.path.join(dataset,file)).read()
		rows = [row.split(';') for row in data.split('\n')]
		df=pd.DataFrame(rows,columns=['sentence','label'])
	# Dictionary mapping category -> new value                    
	mapping = {'1': 'positive', '-1': 'negative', '0':'neutral'}

	# Replace values where category matches mapping keys
	df['label'] = df['label'].sample(frac=1).map(mapping).fillna(df['label'])
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'aeb_Latn-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'aeb_Latn-test.csv'),index=False)

def process_dzsenti(dataset,datapath):

	df = pd.read_csv(os.path.join(dataset,'dataset.csv'))
	df.drop(columns=['id'],inplace=True)
	df.rename(columns={"text": "sentence", "sentiment": "label"},inplace=True)      
	# Dictionary mapping category -> new value                    
	mapping = {'Positive': 'positive', 'Negative': 'negative'}

	# Replace values where category matches mapping keys
	df['label'] = df['label'].sample(frac=1).map(mapping).fillna(df['label'])
	print(df['label'].value_counts())
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'arq_arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'arq_arab-test.csv'),index=False)

def process_mac(dataset,datapath):

	df = pd.read_csv(os.path.join(dataset,'MAC corpus.csv'))
	df.rename(columns={"tweets": "sentence", "type": "label"},inplace=True)      
	df_msa=df[df['class']=='standard']
	df_ary=df[df['class']=='dialectal']
	df_msa.drop(columns=['class'],inplace=True)
	df_ary.drop(columns=['class'],inplace=True)
	
	print(df_msa['label'].value_counts())
	print(df_ary['label'].value_counts())
	
	df=df_msa
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'arb_arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'arb_arab-test.csv'),index=False)

	df=df_ary
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'ary_arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'ary_arab-test.csv'),index=False)

def process_saudi(dataset,datapath):

	# Load sheet into DataFrame 
	df = pd.read_excel(os.path.join(dataset,'data_Saudi_banks.xlsx'), sheet_name='Sheet1')
	df=df[['Tweet','Final annotation']]
	df.rename(columns={"Tweet": "sentence", "Final annotation": "label"},inplace=True)
	# Dictionary mapping category -> new value                    
	mapping = {'POS': 'positive', 'NEG': 'negative','NEU':'neutral'}

	# Replace values where category matches mapping keys
	df['label'] = df['label'].sample(frac=1).map(mapping).fillna(df['label'])      
	print(df.head(10))
	print(df['label'].value_counts())
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'sau_arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'sau_arab-test.csv'),index=False)

def process_astd(dataset,datapath):
	data = open(os.path.join(dataset,'data/Tweets.txt')).read()
	rows = [row.split('\t') for row in data.split('\n')]
	df=pd.DataFrame(rows,columns=['sentence','label'])
	print(df['label'].value_counts())
	mapping = {'POS': 'positive', 'NEG': 'negative','NEUTRAL':'neutral','OBJ':'objective'}
	# Replace values where category matches mapping keys
	df['label'] = df['label'].sample(frac=1).map(mapping).fillna(df['label'])  
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	print('train:\n',train_df['label'].value_counts(), 'test:\n',test_df['label'].value_counts())
	train_df.to_csv(os.path.join(datapath,'arz_arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'arz_arab-test.csv'),index=False)

def process_ajgt(dataset,datapath):

	# Load sheet into DataFrame 
	df = pd.read_excel(os.path.join(dataset,'AJGT.xlsx'), sheet_name='1')
	df=df[['Feed','Sentiment']]
	df.rename(columns={"Feed": "sentence", "Sentiment": "label"},inplace=True)
	# # Dictionary mapping category -> new value                    
	mapping = {'Positive': 'positive', 'Negative': 'negative','NEU':'neutral'}

	# Replace values where category matches mapping keys
	df['label'] = df['label'].sample(frac=1).map(mapping).fillna(df['label'])      
	print(df.head(10))
	print(df['label'].value_counts())
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'jor_arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'jor_arab-test.csv'),index=False)

def process_oclar(dataset,datapath):
	url="http://archive.ics.uci.edu/ml/machine-learning-databases/00499/OCLAR%20-%20Opinion%20Corpus%20for%20Lebanese%20Arabic%20Reviews.csv"
	df=pd.read_csv(url)

	df.rename(columns={"review": "sentence", "rating": "label"},inplace=True)
   
	print(df.head(10))
	print(df['label'].value_counts())
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'ar-lb_arab-train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'ar-lb_arab-test.csv'),index=False)

def process_greek(dataset,datapath):
	files = ['cg_fb.txt','cg_other.txt','cg_twitter.txt','smg_fb.txt','smg_other.txt','smg_twitter.txt']
	all_data={}
	all_df=pd.DataFrame()
	for file in files:
		data = open(os.path.join(dataset,'Data',file)).read()
		rows = [row for row in data.split('\n')]
		df=pd.DataFrame(rows,columns=['sentence'])
		df['label']=file.split('.')[0]
		all_df = pd.concat([all_df,df])
	df=all_df.copy()
	print(df['label'].value_counts())
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'test.csv'),index=False)

def process_dsltl(dataset,datapath):
	folders={'english':'EN-DSL-TL',
			'spanish':'ES-DSL-TL',
			'portuguese':'PT-DSL-TL'}
	for lang,fol in folders.items():
		dev_file=os.path.join(dataset,'DSL-TL-Corpus',fol,'{}_dev.tsv'.format(fol.split('-')[0]))
		train_file=os.path.join(dataset,'DSL-TL-Corpus',fol,'{}_train.tsv'.format(fol.split('-')[0]))
		dev_df = pd.read_csv(dev_file, sep='\t',header=None).sample(frac=1)
		dev_df.columns=['id','sentence','label']
		train_df = pd.read_csv(dev_file, sep='\t',header=None).sample(frac=1)
		train_df.columns=['id','sentence','label']
		print('train:',train_df['label'].value_counts())
		print('dev:',dev_df['label'].value_counts())
		train_df.to_csv(os.path.join(datapath,lang+'-train.csv'),index=False)
		dev_df.to_csv(os.path.join(datapath,lang+'-dev.csv'),index=False)


def process_archimob(dataset,datapath):
	dataset = load_dataset(dataset)
	sentences=dataset['train']['sentence']
	labels=dataset['train']['label']
	df=pd.DataFrame(zip(sentences,labels),columns=['sentence','label'])
	train_df, test_df = train_test_split(df.sample(frac=1), test_size=0.3)
	print('train:{}, test:{}'.format(len(train_df),len(test_df)))
	train_df.to_csv(os.path.join(datapath,'train.csv'),index=False)
	test_df.to_csv(os.path.join(datapath,'test.csv'),index=False)

def process_dmt(dataset,datapath):
	folders={'mandarin_simplified':'raw_data/TRAININGSET-DMT_SIMP-VARDIAL2019',
			'mandarin_traditional':'raw_data/TRAININGSET-DMT_TRAD-VARDIAL2019',}

	for lang,fol in folders.items():
		dev_file=os.path.join(dataset,fol,'dev.txt')
		train_file=os.path.join(dataset,fol,'train.txt')
		dev_df = pd.read_csv(dev_file, sep='\t',header=None).sample(frac=1)
		dev_df.columns=['sentence','label']
		train_df = pd.read_csv(dev_file, sep='\t',header=None).sample(frac=1)
		train_df.columns=['sentence','label']
		print(train_df.head(10))
		print('train:',train_df['label'].value_counts())
		print(dev_df.head(10))
		print('dev:',dev_df['label'].value_counts())
		train_df.to_csv(os.path.join(datapath,lang+'-train.csv'),index=False)
		dev_df.to_csv(os.path.join(datapath,lang+'-dev.csv'),index=False)



def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-datapath', '--datapath', type=str, help='data folder location', required=True)
    parser.add_argument('-dataset', '--dataset', type=str, help='dataset name', required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    
    args = get_arguments()
    print(args)

    datapath=args.datapath
    dataset=args.dataset
    if dataset=='madar':
    	process_madar(datapath)
    if dataset=='TSAC':
    	process_tasc(dataset,datapath)
    if dataset=='TUNIZI':
    	process_tunizi(dataset,datapath)
    if dataset=='DzSentiA':
    	process_dzsenti(dataset,datapath)
    if dataset=='Saudi-Bank-Sentiment-Dataset':
    	process_saudi(dataset,datapath)
    if dataset=='MAC':
    	process_mac(dataset,datapath)
    if dataset=='ASTD':
    	process_astd(dataset,datapath)
    if dataset=='Arabic-twitter-corpus-AJGT':
    	process_ajgt(dataset,datapath)
    if dataset=='oclar':
    	process_oclar(dataset,datapath)
    if dataset=='greek-dialect-classifier':
    	process_greek(dataset,datapath)
    if dataset=='DSL-TL':
    	process_dsltl(dataset,datapath)
    if dataset=='statworx/swiss-dialects':
    	process_archimob(dataset,datapath)
    if dataset=='DMT':
    	process_dmt(dataset,datapath)

# python scripts/dialect_identification/process_dataset.py --dataset madar --datapath data/dialect-identification/arabic/MADAR/MADAR_Corpus