#!/bin/bash
task=${task:-none}
lang=${lang:-eng}
lang2=${lang2:-eng}
lang3=${lang3:-eng}
MODEL_NAME=${MODEL_NAME:-bert}
CACHE_DIR=${CACHE_DIR:-'/scratch/ffaisal/hug_cache/datasets/DialectBench'}
dataset=${dataset:-wikiann}
prefix_text=${prefix_text:-prefix_text}
 
# RESULT_FOLDER="/projects/antonis/fahim/DialectBench/experiments"
RESULT_FOLDER="/projects/antonis/fahim/DialectBench/results"
mkdir ${RESULT_FOLDER}


while [ $# -gt 0 ]; do

   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
        echo $1 $2 #Optional to see the parameter:value result
   fi

  shift
done

if [[ "$MODEL_NAME" = "bert" ]]; then
	MODEL_PATH='bert-base-multilingual-cased'
fi

if [[ "$MODEL_NAME" = "xlmr" ]]; then
	MODEL_PATH='xlm-roberta-base'
fi

echo ${task}
echo ${lang}
echo ${MODEL_NAME}
echo ${CACHE_DIR}

module load python/3.8.6-ff
cd /scratch/ffaisal/DialectBench

if [[ "$task" = "install_adapter_latest" || "$task" = "all" ]]; then
	echo "------------------------------Install adapter latest------------------------------"
	module load python/3.8.6-ff
	rm -rf adapter-transformers-l
	rm -rf vnv/vnv-adp-l
	python -m venv vnv/vnv-adp-l
	source vnv/vnv-adp-l/bin/activate
	wget -O adapters3.1.0.tar.gz https://github.com/adapter-hub/adapter-transformers/archive/refs/tags/adapters3.1.0.tar.gz
	tar -xf adapters3.1.0.tar.gz
	rm adapters3.1.0.tar.gz
	mv adapter-transformers-adapters3.1.0 adapter-transformers-l
	cd adapter-transformers-l
	#cp ../scripts/ad_l_trans_trainer.py src/transformers/trainer.py
	pip install .
	../vnv/vnv-adp-l/bin/python -m pip install --upgrade pip
	cd ..
	pip install --upgrade pip
	pip3 install -r requirements.txt
	##for A100 gpu
	deactivate
fi

if [[ "$task" = "install_transformers_latest" || "$task" = "all" ]]; then
	module load python/3.8.6-ff
	rm -rf transformers-orig
	rm -rf vnv/vnv-trns
	module load python/3.8.6-ff
	python -m venv vnv/vnv-trns
	source vnv/vnv-trns/bin/activate
	wget -O transformersv4.21.1.tar.gz "https://github.com/huggingface/transformers/archive/refs/tags/v4.21.1.tar.gz"
	tar -xf transformersv4.21.1.tar.gz
	rm transformersv4.21.1.tar.gz
	mv transformers-4.21.1 transformers-orig
	cd transformers-orig
	pip install .
	pip install --upgrade pip
	cd ..
	pip install -r requirements.txt
	deactivate
fi

if [[ "$task" = "install_transformers_qa" || "$task" = "all" ]]; then
	module load python/3.8.6-ff
	rm -rf vnv/vnv-qa
	module load python/3.8.6-ff
	python -m venv vnv/vnv-qa
	source vnv/vnv-qa/bin/activate
	pip install transformers==3.4.0
	pip install --upgrade pip
	pip install -r requirements.txt
	deactivate
fi


if [[ "$task" = "train_udp" || "$task" = "all" ]]; then

	echo "------------------------------Train UDP------------------------------"
	source vnv/vnv-adp-l/bin/activate

	export TASK_NAME=${lang}

	python scripts/run_udp.py \
	    --model_name_or_path ${MODEL_PATH} \
	    --do_train \
	    --task_name $TASK_NAME \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-4 \
	    --num_train_epochs 5 \
	    --max_seq_length 256 \
	    --cache_dir ${CACHE_DIR} \
	    --output_dir /projects/antonis/fahim/DialectBench/experiments/${MODEL_NAME}/$TASK_NAME \
	    --overwrite_output_dir \
	    --store_best_model \
	    --evaluation_strategy epoch \
	    --metric_score las  \
	    --save_strategy no
	deactivate
fi


if [[ "$task" = "predict_udp" || "$task" = "all" ]]; then

	echo "------------------------------Predict UDP------------------------------"
	source vnv/vnv-adp-l/bin/activate
	export TASK_NAME="UD_English-EWT"

	##few shot
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_all.txt"
	rm ${result_file} 
	python scripts/run_udp.py \
	    --model_name_or_path ${MODEL_PATH} \
	    --do_predict_all \
	    --task_name $TASK_NAME \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-4 \
	    --num_train_epochs 5 \
	    --max_seq_length 256 \
	    --cache_dir ${CACHE_DIR} \
	    --lang_config metadata/udp_metadata.json \
	    --result_file ${result_file} \
	    --output_dir /projects/antonis/fahim/DialectBench/experiments/${MODEL_NAME} \
	    --evaluation_strategy epoch \
	    --metric_score las

	##zero shot
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${TASK_NAME}.txt"
	rm ${result_file} 

	python scripts/run_udp.py \
	    --model_name_or_path ${MODEL_PATH} \
	    --do_predict_all \
	    --use_train_lang \
	    --task_name $TASK_NAME \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-4 \
	    --num_train_epochs 5 \
	    --max_seq_length 256 \
	    --cache_dir ${CACHE_DIR} \
	    --lang_config metadata/udp_metadata.json \
	    --result_file ${result_file} \
	    --output_dir /projects/antonis/fahim/DialectBench/experiments/${MODEL_NAME} \
	    --evaluation_strategy epoch \
	    --metric_score las
	deactivate
fi



if [[ "$task" = "train_sdqa" || "$task" = "all" ]]; then

	echo "------------------------------Train SD-QA------------------------------"

	source vnv/vnv-qa/bin/activate
	output_dir="/projects/antonis/fahim/DialectBench/experiments/${MODEL_NAME}/sdqa/${lang}"

	##train_all
	python scripts/run_squad.py \
		--model_type ${MODEL_NAME} \
		--model_name_or_path ${MODEL_PATH} \
		--prefix ${lang} \
		--do_train \
		--split train \
		--do_lower_case \
		--train_file "data/Question-Answering/SDQA-gold-task/sdqa-train-${lang}.json" \
		--per_gpu_train_batch_size 16 \
		--per_gpu_eval_batch_size 24 \
		--learning_rate 3e-5 \
		--num_train_epochs 5 \
		--max_seq_length 384 \
		--doc_stride 128 \
		--cache_dir ${CACHE_DIR} \
		--output_dir ${output_dir} \
		--overwrite_output_dir \
		--save_steps 3000 \
		--overwrite_cache

	rm -rf ${output_dir}/checkpoint*
	deactivate
fi

if [[ "$task" = "predict_sdqa" || "$task" = "all" ]]; then

	echo "------------------------------Predict SD-QA------------------------------"

	source vnv/vnv-qa/bin/activate
	output_dir="/projects/antonis/fahim/DialectBench/experiments/${MODEL_NAME}/sdqa/${lang}"
	predict_file="data/Question-Answering/SDQA-gold-task/sdqa-${dataset}-all.json"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
	rm -rf ${result_file}

	##predict_all
	python scripts/run_squad.py \
		--model_type ${MODEL_NAME} \
		--model_name_or_path ${output_dir} \
		--prefix ${lang} \
		--split ${dataset} \
		--do_eval \
		--predict_file ${predict_file} \
		--do_lower_case \
		--per_gpu_train_batch_size 16 \
		--per_gpu_eval_batch_size 24 \
		--learning_rate 3e-5 \
		--num_train_epochs 5 \
		--max_seq_length 384 \
		--doc_stride 128 \
		--cache_dir ${CACHE_DIR} \
		--output_dir ${output_dir} \
		--result_file ${result_file} \
		--save_steps 3000

	rm -rf ${output_dir}/checkpoint*
	deactivate
fi

if [[ "$task" = "train_ner" || "$task" = "all" ]]; then

	echo "------------------------------Train NER------------------------------"
	# source vnv/vnv-adp-l/bin/activate
	export TASK_NAME="ner"
	# export TASK_NAME="UD_French-ParTUT"
	source vnv/vnv-trns/bin/activate

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/ner/${lang}"

	##norwegian
	python scripts/ner/run_ner.py \
	  --model_name_or_path ${MODEL_PATH} \
	  --dataset_name ${dataset} \
	  --dataset_config_name ${lang} \
	  --task_name ner \
	  --max_seq_length 128 \
	  --per_device_train_batch_size 32 \
	  --learning_rate 2e-5 \
	  --num_train_epochs 5 \
	  --output_dir ${output_dir} \
	  --overwrite_output_dir \
	  --do_train \
	  --save_strategy no \
	  --cache_dir ${CACHE_DIR} \
	  --overwrite_cache
	  # --max_steps 1

	deactivate
	rm -rf ${output_dir}/checkpoint*
fi

if [[ "$task" = "train_did_lm" || "$task" = "all" ]]; then

	echo "------------------------------Train dialect-identification using mBERT/XLM-R------------------------------"
	source vnv/vnv-trns/bin/activate

	train_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/train.csv"
	dev_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/dev.csv"

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/did/${lang}_${dataset}"

	python scripts/dialect_identification/text-classification_transformers.py \
	    --model_name_or_path ${MODEL_PATH} \
	    --train_file ${train_file} \
	    --validation_file ${dev_file} \
	    --shuffle_train_dataset \
	    --metric_name accuracy \
	    --do_train \
	    --do_eval \
	    --max_seq_length 512 \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-5 \
	    --num_train_epochs 5 \
	    --cache_dir ${CACHE_DIR} \
	    --output_dir ${output_dir} \
	    --save_strategy no \
	    --overwrite_output_dir
	deactivate
	rm -rf ${output_dir}/checkpoint*
fi

if [[ "$task" = "train_predict_did_ml" || "$task" = "all" ]]; then

	echo "------------------------------Train dialect-identification using ml algorithms------------------------------"
	source vnv/vnv-trns/bin/activate

	train_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/train.csv"
	test_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/test.csv"
	dev_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/dev.csv"

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/did/${lang}_${dataset}"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
	rm -rf result_file

	python scripts/dialect_identification/classification-ml.py \
	--datapath data/dialect-identification/arabic/MADAR/MADAR_Corpus \
	--dataset ${dataset} \
	--lang ${lang} \
	--model ${MODEL_NAME} \
	--sent_column sentence \
	--label_column label \
	--result_file ${result_file}
	deactivate
	rm -rf ${output_dir}/checkpoint*
fi

if [[ "$task" = "predict_did_lm" || "$task" = "all" ]]; then

	echo "------------------------------Train dialect-identification using mBERT/XLM-R------------------------------"
	source vnv/vnv-trns/bin/activate

	train_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/train.csv"
	dev_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/dev.csv"
	test_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/test.csv"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
	rm -rf result_file

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/did/${lang}_${dataset}"

	python scripts/dialect_identification/text-classification_transformers.py \
	    --model_name_or_path ${output_dir} \
	    --train_file ${train_file} \
	    --validation_file ${dev_file} \
	    --test_file ${test_file} \
	    --shuffle_train_dataset \
	    --metric_name accuracy \
	    --prefix ${lang}_${dataset} \
	    --result_file ${result_file} \
	    --do_predict \
	    --max_seq_length 512 \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-5 \
	    --num_train_epochs 5 \
	    --cache_dir ${CACHE_DIR} \
	    --output_dir ${output_dir}

	deactivate
fi


if [[ "$task" = "train_reading_comprehension" || "$task" = "all" ]]; then

	echo "----------------------training reading comprehension multiple choice quesiton answering------------------------------"

	source vnv/vnv-trns/bin/activate
	train_file="data/reading-comprehension/Belebele/${lang}.jsonl"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/rc/${lang}_${dataset}"


	python scripts/run_swag.py \
	--model_name_or_path ${MODEL_PATH}\
	--do_train \
	--train_file ${train_file} \
	--validation_file ${train_file} \
	--learning_rate 5e-5 \
	--num_train_epochs 5 \
	--per_device_eval_batch_size=16 \
	--per_device_train_batch_size=16 \
	--overwrite_output \
	--output_dir ${output_dir} \
	--max_seq_length 128 \
	--cache_dir ${CACHE_DIR} \
	--overwrite_cache
	# --max_steps 10

	deactivate
fi


if [[ "$task" = "predict_reading_comprehension" || "$task" = "all" ]]; then

	echo "----------------------training reading comprehension multiple choice quesiton answering------------------------------"

	source vnv/vnv-trns/bin/activate
	train_file="data/reading-comprehension/Belebele/${lang}.jsonl"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/rc/${lang}_${dataset}"

	data_dir="data/reading-comprehension/Belebele"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
	rm -rf result_file


	python scripts/run_swag.py \
	--model_name_or_path ${output_dir}\
	--do_predict_all \
	--train_file ${train_file} \
	--validation_file ${train_file} \
	--lang_config metadata/rcmc_metadata.json \
	--data_dir ${data_dir} \
	--learning_rate 5e-5 \
	--num_train_epochs 5 \
	--per_device_eval_batch_size=16 \
	--per_device_train_batch_size=16 \
	--output_dir ${output_dir} \
	--prefix ${lang}_${dataset} \
	--result_file ${result_file} \
	--max_seq_length 128 \
	--cache_dir ${CACHE_DIR}
	# --max_steps 10

	deactivate
fi


if [[ "$task" = "predict_udp_test" || "$task" = "all" ]]; then

	echo "----------------------training reading comprehension multiple choice quesiton answering------------------------------"

	source vnv/vnv-trns/bin/activate
	lang="eng_Latn"
	dataset="Belebele"
	train_file="data/reading-comprehension/Belebele/${lang}.jsonl"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/rc/${lang}_${dataset}"

	data_dir="data/reading-comprehension/Belebele"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
	rm -rf result_file


	python scripts/run_swag.py \
	--model_name_or_path ${output_dir}\
	--do_predict_all \
	--train_file ${train_file} \
	--validation_file ${train_file} \
	--lang_config metadata/rcmc_metadata.json \
	--data_dir ${data_dir} \
	--learning_rate 5e-5 \
	--num_train_epochs 5 \
	--per_device_eval_batch_size=16 \
	--per_device_train_batch_size=16 \
	--output_dir ${output_dir} \
	--prefix ${lang}_${dataset} \
	--result_file ${result_file} \
	--max_seq_length 128 \
	--cache_dir ${CACHE_DIR}
	# --max_steps 10

	deactivate
fi

if [[ "$task" = "create_sib_topic_classification" || "$task" = "all" ]]; then

	echo "------------------------------Create SIB-200 dataset------------------------------"
	##code taken and adapted from https://github.com/dadelani/sib-200/tree/main
	source vnv/vnv-trns/bin/activate

	mkdir -p data
	mkdir -p data/raw

	# download flores200
	wget --trust-server-names https://tinyurl.com/flores200dataset

	# unzip downloaded files.
	tar -xvzf flores200_dataset.tar.gz

	for split in dev devtest
	do
	  dir_name=flores200_dataset/$split
	    for filename in "$dir_name"/*
	    do
	      cp -r $filename data/raw/
	      done
	  done
	cp -r flores200_dataset/dev/deu_Latn.dev data/raw/
	cp -r flores200_dataset/devtest/deu_Latn.devtest data/raw/


	# delete archive and unused folders
	rm -rf flores*

	./dgf.sh https://github.com/dadelani/sib-200/tree/main/data/eng

	python scripts/topic-classification/create_sib_data.py
	rm -rf data/raw
	rm -rf sib-200
	deactivate
fi

if [[ "$task" = "train_topic_classification_lm" || "$task" = "all" ]]; then

	echo "------------------------------Train topic-classification using mBERT/XLM-R------------------------------"
	source vnv/vnv-trns/bin/activate

	train_file="data/topic_class/${lang}/train.csv"
	dev_file="data/topic_class/${lang}/dev.csv"
	test_file="data/topic_class/${lang}/test.csv"
	label_file="data/topic_class/${lang}/labels.txt"

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/topic_class/${lang}_${dataset}"

	python scripts/topic-classification/topic-classification_transformers.py \
	    --model_name_or_path ${MODEL_PATH} \
	    --train_file ${train_file} \
	    --validation_file ${dev_file} \
	    --shuffle_train_dataset \
	    --metric_name accuracy \
	    --do_train \
	    --do_eval \
	    --max_seq_length 512 \
	    --per_device_train_batch_size 32 \
	    --learning_rate 1e-5 \
	    --num_train_epochs 5 \
	    --cache_dir ${CACHE_DIR} \
	    --output_dir ${output_dir} \
	    --save_strategy no \
	    --overwrite_output_dir
	    # --max_steps 20
	deactivate
	rm -rf ${output_dir}/checkpoint*
fi

if [[ "$task" = "predict_topic_classification_lm" || "$task" = "all" ]]; then

	echo "------------------------------Predict topic-classification using mBERT/XLM-R------------------------------"
	source vnv/vnv-trns/bin/activate

	train_file="data/topic_class/${lang}/train.csv"
	dev_file="data/topic_class/${lang}/dev.csv"
	test_file="data/topic_class/${lang}/test.csv"
	data_dir="data/topic_class"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
	rm -rf result_file

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/topic_class/${lang}_${dataset}"

	python scripts/topic-classification/topic-classification_transformers.py \
	    --model_name_or_path ${output_dir} \
	    --train_file ${train_file} \
	    --validation_file ${dev_file} \
	    --test_file ${test_file} \
	    --data_dir ${data_dir} \
	    --shuffle_train_dataset \
	    --metric_name accuracy \
	    --prefix ${lang}_${dataset} \
	    --result_file ${result_file} \
	    --do_predict_all \
	    --lang_config metadata/topic_metadata.json \
	    --max_seq_length 512 \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-5 \
	    --num_train_epochs 5 \
	    --cache_dir ${CACHE_DIR} \
	    --output_dir ${output_dir}

	deactivate
fi


if [[ "$task" = "download_udp_train" || "$task" = "all" ]]; then
	echo "-------------------------------Download UDP all train data-----------------------------"
	cd data
	wget -O udp_all_train.zip https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EZRJRItvJ9ZCsykKm8MZlwcBuMF8Va3kShpHcg4JqT3yxg?download=1
	module load openjdk/11.0.2-qg
	jar -xf udp_all_train.zip
	rm udp_all_train.zip
	module unload openjdk/11.0.2-qg
	cd ..
fi

if [[ "$task" = "download_ner_train" || "$task" = "all" ]]; then
	echo "-------------------------------Download NER all train data-----------------------------"
	cd data
	wget -O ner_all_train.zip https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EVidvsVS7s1CuY2EcwpQ9bABip-n0Trjc2bfgmS7QlOlOg?download=1
	wget -O m2ner_all_train.zip https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EU1D43O4S1ZInHRTAygJpP8BEf08x9X0Kj7TTbPMvsr6vw?download=1
	module load openjdk/11.0.2-qg
	jar -xf ner_all_train.zip
	jar -xf m2ner_all_train.zip
	rm ner_all_train.zip
	rm m2ner_all_train.zip
	module unload openjdk/11.0.2-qg
	cd ..
fi


function download_panx {
    echo "Download panx NER dataset"
    if [ -f $DIR/AmazonPhotos.zip ]; then
        base_dir=$DIR/panx_dataset/
        unzip -qq -j $DIR/AmazonPhotos.zip -d $base_dir
        cd $base_dir
        langs=(ar he vi id jv ms tl eu ml ta te af nl en de el bn hi mr ur fa fr it pt es bg ru ja ka ko th sw yo my zh kk tr et fi hu qu pl uk az lt pa gu ro)
        for lg in ${langs[@]}; do
            tar xzf $base_dir/${lg}.tar.gz
            for f in dev test train; do mv $base_dir/$f $base_dir/${lg}-${f}; done
        done
        cd ..
        python $REPO/utils_preprocess.py \
            --data_dir $base_dir \
            --output_dir $DIR/panx \
            --task panx
        rm -rf $base_dir
        echo "Successfully downloaded data at $DIR/panx" >> $DIR/download.log
    else
        echo "Please download the AmazonPhotos.zip file on Amazon Cloud Drive manually and save it to $DIR/AmazonPhotos.zip"
        echo "https://www.amazon.com/clouddrive/share/d3KGCRCIYwhKJF0H3eWA26hjg2ZCRhjpEQtDL70FSBN"
    fi
}
