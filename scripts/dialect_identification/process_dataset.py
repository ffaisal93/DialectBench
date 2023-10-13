import csv
import os
import pandas as pd
import argparse



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

# python scripts/dialect_identification/process_dataset.py --dataset madar --datapath data/dialect-identification/arabic/MADAR/MADAR_Corpus