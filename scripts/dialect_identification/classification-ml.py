import csv
import os
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
"""
python scripts/dialect_identification/classification-ml.py \
--datapath data/dialect-identification/arabic/MADAR/MADAR_Corpus \
--dataset madar \
--lang arabic \
--model nb \
--sent_column sentence \
--label_column label \
--result_file test/test-result.txt
"""



def get_data(datapath):
	train_df=pd.read_csv(os.path.join(datapath,'train.csv'))
	test_df=pd.read_csv(os.path.join(datapath,'test.csv'))
	dev_df=pd.read_csv(os.path.join(datapath,'dev.csv'))

	return {
		'train': train_df[:100],
		'dev': dev_df[:100],
		'test': test_df[:100]
	}

	print(train_df.columns)


def train_randomforest(df, sent_column, label_column):
	X_train = df['train'][sent_column]
	y_train = df['train'][label_column]

	classifier_tfidf_RF = RandomForestClassifier(n_estimators=50)
	model_tfidf_RF = Pipeline([("vectorizer", vectorizer_tfidf), ("classifier", classifier_tfidf_RF)])

	model_tfidf_RF.fit(X_train, y_train)

	predicted_train_tfidf_RF = model_tfidf_RF.predict(X_train)
	accuracy_train_tfidf_RF = accuracy_score(y_train, predicted_train_tfidf_RF)
	print('Accuracy Training data: {:.1%}'.format(accuracy_train_tfidf_RF))

	predicted_test_tfidf_RF = model_tfidf_RF.predict(X_test)
	accuracy_test_tfidf_RF = accuracy_score(y_test, predicted_test_tfidf_RF)
	print('Accuracy Test data: {:.1%}'.format(accuracy_test_tfidf_RF))

def train_nb(df, sent_column, label_column):
	X_train = df['train'][sent_column]
	y_train = df['train'][label_column]

	corpus = X_train
	# Initizalize the vectorizer with max nr words and ngrams (1: single words, 2: two words in a row)
	vectorizer_tfidf = TfidfVectorizer(ngram_range=(1,3))
	# Fit the vectorizer to the training data
	vectorizer_tfidf.fit(corpus)

	classifier_tfidf_NB = MultinomialNB()
	model_tfidf_NB = Pipeline([("vectorizer", vectorizer_tfidf), ("classifier", classifier_tfidf_NB)])
	model_tfidf_NB.fit(X_train, y_train)
	return model_tfidf_NB

def predict(model,df,sent_column, label_column):
	X_test = df['test'][sent_column]
	y_test = df['test'][label_column]


	predicted_test_tfidf_NB = model.predict(X_test)
	accuracy_test_tfidf_NB = accuracy_score(y_test, predicted_test_tfidf_NB)
	print('Accuracy Test data: {:.1%}'.format(accuracy_test_tfidf_NB))
	class_report = classification_report(predicted_test_tfidf_NB,y_test,output_dict=True)
	return class_report

def save_result(class_report, result_file, prefix):
	with open(result_file, "w") as writer:
		for k,v in class_report.items():
			if type(v)==dict:
				writer.write("%s,%s,%s,%s,%s,%s\n" % (prefix,k,v['precision'],v['recall'],v['f1-score'],v['support']))
			else:
				writer.write("%s,%s,%s,%s,%s,%s\n" % (prefix,k,v,0,0,0))
			print(k,v)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', '--model', type=str, help='model to train on', required=True)
    parser.add_argument('-dataset', '--dataset', type=str, help='model to train on', required=True)
    parser.add_argument('-lang', '--lang', type=str, help='language description', required=True)
    parser.add_argument('-datapath', '--datapath', type=str, help='data folder location', required=True)
    parser.add_argument('-sent_column', '--sent_column', type=str, help='sentence column', required=True)
    parser.add_argument('-label_column', '--label_column', type=str, help='label column', required=True)
    parser.add_argument('-result_file', '--result_file', type=str, help='label column', required=True)
    args = parser.parse_args()
    return args

def main():
	args = get_arguments()
	print(args)

	datapath=args.datapath
	dataset=args.dataset
	lang=args.lang
	model_name=args.model
	sent_column = args.sent_column
	label_column = args.label_column
	result_file = args.result_file
	data_df = get_data(datapath)

	if model_name=='nb':
		trained_model=train_nb(data_df,sent_column, label_column)
		class_report = predict(trained_model,data_df,sent_column, label_column)
		save_result(class_report,result_file, lang+'_'+dataset)
	


if __name__ == '__main__':
	main()






