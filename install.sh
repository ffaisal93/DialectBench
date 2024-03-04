#!/bin/bash
task=${task:-none}
execute=${execute:-'bash'}
lang=${lang:-eng}
lang2=${lang2:-eng}
lang3=${lang3:-eng}
MODEL_NAME=${MODEL_NAME:-bert}
CACHE_DIR=${CACHE_DIR:-'/scratch/ffaisal/hug_cache/datasets/DialectBench'}
OUTPUT_DIR=${OUTPUT_DIR:-none}
ROOT_DIR=${ROOT_DIR:-none}
dataset=${dataset:-wikiann}
prefix_text=${prefix_text:-prefix_text}
 
# RESULT_FOLDER="/projects/antonis/fahim/DialectBench/experiments"
ROOT_DIR="/scratch/ffaisal/DialectBench"
RESULT_FOLDER="/scratch/ffaisal/DialectBench/results"
TEST_RESULT_FOLDER="/scratch/ffaisal/DialectBench/test/results"

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

if [[ "$MODEL_NAME" = "xlmrl" ]]; then
	MODEL_PATH='xlm-roberta-large'
fi

if [[ "$execute" = "bash" ]]; then

	if [[ "$ROOT_DIR" = none ]]; then
		ROOT_DIR=${PWD}
	fi
	
	if [[ "$OUTPUT_DIR" = none ]]; then
		OUTPUT_DIR="${ROOT_DIR}/experiments"
		mkdir ${OUTPUT_DIR}
	fi

	if [[ "$CACHE_DIR" = none ]]; then
		CACHE_DIR="cache"
		mkdir ${CACHE_DIR}
	fi

	RESULT_FOLDER="${ROOT_DIR}/results"
	TEST_FOLDER="${ROOT_DIR}/test"
	TEST_RESULT_FOLDER="${ROOT_DIR}/test/results"

	mkdir ${RESULT_FOLDER}
	mkdir ${TEST_FOLDER}
	mkdir ${TEST_RESULT_FOLDER}

	cd ${ROOT_DIR}

fi

if [[ "$execute" = "gmu_cluster" ]]; then

	if [[ "$ROOT_DIR" = none ]]; then
		ROOT_DIR="/scratch/ffaisal/DialectBench"
	fi

	if [[ "$OUTPUT_DIR" = none ]]; then
		OUTPUT_DIR="/projects/antonis/fahim/DialectBench/experiments"
		mkdir ${OUTPUT_DIR}
	fi

	if [[ "$CACHE_DIR" = none ]]; then
		CACHE_DIR="/scratch/ffaisal/hug_cache/datasets/DialectBench"
		mkdir ${CACHE_DIR}
	fi

	RESULT_FOLDER="${ROOT_DIR}/results"
	TEST_FOLDER="${ROOT_DIR}/test"
	TEST_RESULT_FOLDER="${ROOT_DIR}/test/results"

	mkdir ${RESULT_FOLDER}
	mkdir ${TEST_FOLDER}
	mkdir ${TEST_RESULT_FOLDER}

	cd ${ROOT_DIR}

	module load git
	module load openjdk/11.0.2-qg
	module load python/3.8.6-ff

fi


echo "task: ${task}"
echo "lang: ${lang}"
echo "model name: ${MODEL_NAME}"
echo "root dir: ${ROOT_DIR}"
echo "cache dir: ${CACHE_DIR}"
echo "result dir: ${RESULT_FOLDER}"
echo "test result dir: ${TEST_RESULT_FOLDER}"
echo "output dir: ${OUTPUT_DIR}"


if [[ "$task" = "install_adapter" || "$task" = "all" ]]; then
	echo "------------------------------Install adapter latest------------------------------"
	rm -rf adapter-transformers-l
	rm -rf vnv/vnv-adp-l
	python -m venv vnv/vnv-adp-l
	source vnv/vnv-adp-l/bin/activate
	wget -O adapters3.1.0.tar.gz https://github.com/adapter-hub/adapter-transformers/archive/refs/tags/adapters3.1.0.tar.gz
	tar -xf adapters3.1.0.tar.gz
	rm adapters3.1.0.tar.gz
	mv adapters-adapters3.1.0 adapter-transformers-l
	cd adapter-transformers-l
	../vnv/vnv-adp-l/bin/python -m pip install --upgrade pip
	##cp ../scripts/ad_l_trans_trainer.py src/transformers/trainer.py
	pip install .
	cd ..
	pip3 install -r requirements.txt
	deactivate
fi

if [[ "$task" = "install_transformers" || "$task" = "all" ]]; then
	rm -rf transformers-orig
	rm -rf vnv/vnv-trns
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
	rm -rf vnv/vnv-qa
	module load python/3.8.6-ff
	source vnv/vnv-qa/bin/activate
	pip install transformers==3.4.0
	pip install --upgrade pip
	pip install -r requirements.txt
	deactivate
fi

if [[ "$task" = "install_transformers_latest" || "$task" = "all" ]]; then
	module load git
	rm -rf vnv/vnv_trans_latest
	python -m venv vnv/vnv_trans_latest
	source vnv/vnv_trans_latest/bin/activate
	pip install --upgrade pip
	ip install torch==2.0.1+cu117 torchvision==0.15.2+cu117 -f https://download.pytorch.org/whl/torch_stable.html
	pip install ipykernel
	pip install git+https://github.com/huggingface/transformers
	pip install "datasets" "accelerate>=0.20.3" "evaluate" tensorboard scikit-learn bitsandbytes
	deactivate

fi

if [[ "$task" = "install_translation" || "$task" = "all" ]]; then
	module load git
	rm -rf vnv/vnv_translation
	python -m venv vnv/vnv_translation
	source vnv/vnv_translation/bin/activate
	pip install --upgrade pip
	pip install torch==2.0.1+cu117 torchvision==0.15.2+cu117 -f https://download.pytorch.org/whl/torch_stable.html
	pip install ipykernel
	pip install transformers==4.34.0
	##pip install transformers==4.28.0##original
	pip install bitsandbytes
	pip install "datasets" "accelerate>=0.20.3" "evaluate" tensorboard scikit-learn
	/scratch/ffaisal/DialectBench/vnv/vnv_translation/bin/python -m ipykernel install --user --name 'transl'
	cd scripts/translation_nli
	git clone https://github.com/ikergarcia1996/Easy-Translate.git
	cd ${ROOT_DIR}
	deactivate

fi

if [[ "$task" = "download_xnli" || "$task" = "all" ]]; then
	source vnv/vnv_translation/bin/activate
	rm -rf tempdata
	mkdir tempdata
	python scripts/translation_nli/save_data.py
	deactivate
fi

if [[ "$task" = "translate_nli" || "$task" = "all" ]]; then
	##lang codes: https://github.com/facebookresearch/flores/blob/main/flores200/README.md#languages-in-flores-200
	source vnv/vnv_translation/bin/activate
	# rm -rf tempdata
	# mkdir tempdata
	# python scripts/translation_nli/save_data.py

	start=`date +%s`
	python scripts/translation_nli/Easy-Translate/translate.py \
	--sentences_path ${dataset} \
	--output_path tempdata/${MODEL_NAME}-${lang}.txt \
	--source_lang eng_Latn \
	--target_lang ${lang} \
	--model_name  /projects/antonis/fahim/models/nllb-200-3.3B \
	--precision 8 \
	--starting_batch_size 128
	
	end=`date +%s`
	min=60
	runtime=$((end-start))
	echo "runtime----------" $((runtime/min))

	deactivate


fi

if [[ "$task" = "process_translate_nli" || "$task" = "all" ]]; then
	source vnv/vnv_translation/bin/activate
	python scripts/translation_nli/process_nli.py

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
	    --output_dir ${OUTPUT_DIR}/${MODEL_NAME}/$TASK_NAME \
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

if [[ "$task" = "train_pos" || "$task" = "all" ]]; 
then

	echo "------------------------------Train POS Tagging------------------------------"
	source vnv/vnv-trns/bin/activate
	# lang="UD_English-EWT"
	# # lang="UD_North_Sami-Giella"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/pos/${lang}"

	python scripts/pos_tagging/run_pos_tagging.py \
	  --model_name_or_path ${MODEL_PATH} \
	  --dataset_name ${dataset} \
	  --ud_script scripts/universal_dependencies.py \
	  --dataset_config_name ${lang} \
	  --max_seq_length 128 \
	  --per_device_train_batch_size 32 \
	  --learning_rate 2e-5 \
	  --num_train_epochs 5 \
	  --output_dir ${output_dir} \
	  --overwrite_output_dir \
	  --do_train \
	  --do_eval \
	  --label_column_name upos \
	  --text_column_name tokens \
	  --cache_dir ${CACHE_DIR} \
	  --overwrite_cache \
	  --save_total_limit 2 \
	  --save_steps 50 \
	  --eval_steps 50 \
	  --save_strategy="steps" \
	  --evaluation_strategy="steps" \
	  --load_best_model_at_end True

	deactivate
	rm -rf ${output_dir}/checkpoint*

fi

if [[ "$task" = "predict_pos" || "$task" = "all" ]]; 
then

	echo "------------------------------Train POS Tagging------------------------------"
	# source vnv/vnv-adp-l/bin/activate
	source vnv/vnv-trns/bin/activate
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_all.txt"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/pos"
	rm ${result_file}
	python scripts/pos_tagging/run_pos_tagging.py \
	  --model_name_or_path ${MODEL_PATH} \
	  --dataset_name ${dataset} \
	  --ud_script scripts/universal_dependencies.py \
	  --dataset_config_name ${lang} \
	  --max_seq_length 128 \
	  --per_device_train_batch_size 32 \
	  --learning_rate 2e-5 \
	  --num_train_epochs 5 \
	  --output_dir ${output_dir} \
	  --result_file ${result_file} \
	  --lang_config metadata/pos_metadata.json \
	  --ud_script scripts/universal_dependencies.py \
	  --noisy_dl_script scripts/pos_tagging/noisy_dialect.py \
	  --noisy_data_dir data/pos_tagging \
	  --overwrite_output_dir \
	  --do_predict_all \
	  --label_column_name upos \
	  --text_column_name tokens \
	  --cache_dir ${CACHE_DIR} \
	  --overwrite_cache \
	  --save_total_limit 2 \
	  --save_steps 500 \
	  --eval_steps 500 \
	  --save_strategy="steps" \
	  --evaluation_strategy="steps" \
	  --load_best_model_at_end True

	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}.txt"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/pos"
	rm ${result_file}
	python scripts/pos_tagging/run_pos_tagging.py \
	  --model_name_or_path ${MODEL_PATH} \
	  --dataset_name ${dataset} \
	  --ud_script scripts/universal_dependencies.py \
	  --dataset_config_name ${lang} \
	  --max_seq_length 128 \
	  --per_device_train_batch_size 32 \
	  --learning_rate 2e-5 \
	  --num_train_epochs 5 \
	  --output_dir ${output_dir} \
	  --result_file ${result_file} \
	  --lang_config metadata/pos_metadata.json \
	  --ud_script scripts/universal_dependencies.py \
	  --noisy_dl_script scripts/pos_tagging/noisy_dialect.py \
	  --noisy_data_dir data/pos_tagging \
	  --overwrite_output_dir \
	  --do_predict_all \
	  --is_zero_shot \
	  --label_column_name upos \
	  --text_column_name tokens \
	  --cache_dir ${CACHE_DIR} \
	  --overwrite_cache \
	  --save_total_limit 2 \
	  --save_steps 500 \
	  --eval_steps 500 \
	  --save_strategy="steps" \
	  --evaluation_strategy="steps" \
	  --load_best_model_at_end True

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

if [[ "$task" = "predict_ner" || "$task" = "all" ]]; then

	echo "------------------------------Train NER------------------------------"
	# source vnv/vnv-adp-l/bin/activate
	export TASK_NAME="ner"
	# export TASK_NAME="UD_French-ParTUT"
	source vnv/vnv-trns/bin/activate

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/ner"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_all.txt"
	rm -rf ${result_file}

	###fine-tune
	python scripts/ner/run_ner.py \
	  --model_name_or_path ${MODEL_PATH} \
	  --dataset_name ${dataset} \
	  --dataset_config_name en \
	  --task_name ner \
	  --max_seq_length 128 \
	  --per_device_train_batch_size 32 \
	  --learning_rate 2e-5 \
	  --num_train_epochs 5 \
	  --output_dir ${output_dir} \
	  --do_predict_all \
	  --save_strategy no \
	  --cache_dir ${CACHE_DIR} \
	  --lang_config metadata/ner_metadata.json \
	  --result_file ${result_file}
	  # --max_steps 1

	###zero-shot
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_en.txt"
	rm -rf ${result_file}
	python scripts/ner/run_ner.py \
	  --model_name_or_path ${MODEL_PATH} \
	  --dataset_name ${dataset} \
	  --dataset_config_name en \
	  --task_name ner \
	  --max_seq_length 128 \
	  --per_device_train_batch_size 32 \
	  --learning_rate 2e-5 \
	  --num_train_epochs 5 \
	  --output_dir ${output_dir} \
	  --do_predict_all \
	  --save_strategy no \
	  --cache_dir ${CACHE_DIR} \
	  --lang_config metadata/ner_metadata.json \
	  --result_file ${result_file} \
	  --is_zero_shot
	  # --max_steps 1
	deactivate
fi

if [[ "$task" = "train_did_lm" || "$task" = "all" ]]; then

	echo "------------------------------Train dialect-identification using mBERT/XLM-R------------------------------"
	source vnv/vnv-trns/bin/activate


	if [[ "$lang" = "arabic" ]]; 
	then
		train_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/train.csv"
		dev_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/dev.csv"
		output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/did/${lang}_${dataset}"
		do_eval=True

		python scripts/dialect_identification/text-classification_transformers.py \
	    --model_name_or_path ${MODEL_PATH} \
	    --train_file ${train_file} \
	    --validation_file ${dev_file} \
	    --shuffle_train_dataset \
	    --metric_name accuracy \
	    --do_train \
	    --do_eval ${do_eval}\
	    --max_seq_length 512 \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-5 \
	    --num_train_epochs 5 \
	    --cache_dir ${CACHE_DIR} \
	    --output_dir ${output_dir} \
	    --save_strategy no \
	    --overwrite_output_dir
	fi

	if [[ "$lang" = "english" || "$lang" = "greek" || "$lang" = "mandarin_simplified" || "$lang" = "mandarin_traditional" || "$lang" = "portuguese" || "$lang" = "spanish" || "$lang" = "swiss-dialects" ]]; 
	then
		train_file="data/dialect-identification/${lang}/train.csv"
		output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/did/${lang}_${dataset}"
		do_eval=False

		python scripts/dialect_identification/text-classification_transformers.py \
	    --model_name_or_path ${MODEL_PATH} \
	    --train_file ${train_file} \
	    --shuffle_train_dataset \
	    --metric_name accuracy \
	    --do_train \
	    --do_eval ${do_eval}\
	    --max_seq_length 512 \
	    --per_device_train_batch_size 32 \
	    --learning_rate 2e-5 \
	    --num_train_epochs 5 \
	    --cache_dir ${CACHE_DIR} \
	    --output_dir ${output_dir} \
	    --save_strategy no \
	    --overwrite_output_dir
	fi
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
	rm -rf ${result_file}

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

	if [[ "$lang" = "arabic" ]]; 
	then
		train_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/train.csv"
		dev_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/dev.csv"
		test_file="data/dialect-identification/arabic/MADAR/MADAR_Corpus/test.csv"
		result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
		rm -rf ${result_file}

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
	fi

	if [[ "$lang" = "english" || "$lang" = "mandarin_simplified" || "$lang" = "mandarin_traditional" || "$lang" = "portuguese" || "$lang" = "spanish" ]]; 
	then
		train_file="data/dialect-identification/${lang}/train.csv"
		test_file="data/dialect-identification/${lang}/dev.csv"
		result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
		rm -rf ${result_file}

		output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/did/${lang}_${dataset}"

	fi

	if [[ "$lang" = "greek" || "$lang" = "swiss-dialects" ]]; 
	then
		train_file="data/dialect-identification/${lang}/train.csv"
		test_file="data/dialect-identification/${lang}/test.csv"
		result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}_${dataset}.txt"
		rm -rf ${result_file}

		output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/did/${lang}_${dataset}"

	fi

	if [[ "$lang" = "english" || "$lang" = "greek" || "$lang" = "mandarin_simplified" || "$lang" = "mandarin_traditional" || "$lang" = "portuguese" || "$lang" = "spanish" || "$lang" = "swiss-dialects" ]]; 
	then
		python scripts/dialect_identification/text-classification_transformers.py \
		    --model_name_or_path ${output_dir} \
		    --train_file ${train_file} \
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

	fi

	deactivate
fi


if [[ "$task" = "assemble_training_set_belebele" || "$task" = "all" ]]; then
	echo "----------------------create belebele training dataset------------------------------"
	source vnv/vnv-trns/bin/activate
	python scripts/reading-comprehension/assemble_training_set.py \
	--downloads_path temp \
	--output_file data/reading-comprehension/Belebele/train.tsv
	deactivate

fi

if [[ "$task" = "train_reading_comprehension" || "$task" = "all" ]]; then

	echo "----------------------training reading comprehension multiple choice quesiton answering------------------------------"

	source vnv/vnv-trns/bin/activate
	train_file="data/reading-comprehension/Belebele/train.jsonl"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/rc/all_${dataset}"


	python scripts/reading-comprehension/run_swag.py \
	--model_name_or_path ${MODEL_PATH}\
	--do_train \
	--do_eval \
	--train_file ${train_file} \
	--prefix "train_combined" \
	--learning_rate 1e-5 \
	--num_train_epochs 3 \
	--per_device_eval_batch_size=16 \
	--per_device_train_batch_size=16 \
	--overwrite_output \
	--output_dir ${output_dir} \
	--max_seq_length 256 \
	--cache_dir ${CACHE_DIR} \
	--overwrite_cache \
	--save_total_limit 5 \
	--save_steps 500 \
	--eval_steps 500 \
	--save_strategy="steps" \
	--evaluation_strategy="steps" \
	--load_best_model_at_end True
	# --max_steps 10

	deactivate
fi


if [[ "$task" = "predict_reading_comprehension" || "$task" = "all" ]]; then

	echo "----------------------predict reading comprehension multiple choice quesiton answering------------------------------"

	source vnv/vnv-trns/bin/activate
	train_file="data/reading-comprehension/Belebele/${lang}.jsonl"
	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/rc/all_${dataset}"

	data_dir="data/reading-comprehension/Belebele"
	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${dataset}.txt"
	rm -rf ${result_file}
	rm -rf ${output_dir}/checkpoint*


	python scripts/reading-comprehension/run_swag.py \
	--model_name_or_path ${output_dir}\
	--do_predict_all \
	--train_file ${train_file} \
	--validation_file ${train_file} \
	--lang_config metadata/rcmc_metadata.json \
	--data_dir ${data_dir} \
	--learning_rate 2e-5 \
	--num_train_epochs 5 \
	--per_device_eval_batch_size=16 \
	--per_device_train_batch_size=16 \
	--output_dir ${output_dir} \
	--prefix all \
	--result_file ${result_file} \
	--max_seq_length 512 \
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

if [[ "$task" = "convert_pos_dataset_to_upos" || "$task" = "all" ]]; then

	echo "arabic dialects================================================"
	rm -rf convert-qcri-4dialects
	rm -rf dialectal_arabic_resources
	git clone https://github.com/mainlp/convert-qcri-4dialects.git
	cd convert-qcri-4dialects
	git clone https://github.com/qcri/dialectal_arabic_resources.git
	# Optional preliminary check:
	python3 check_arabic_segmentation.py dialectal_arabic_resources/seg_plus_pos_egy.txt dialectal_arabic_resources/seg_plus_pos_lev.txt dialectal_arabic_resources/seg_plus_pos_glf.txt dialectal_arabic_resources/seg_plus_pos_mgr.txt  > arabic_preprocessing.log
	# # The actual data conversion:
	python3 convert.py --dir dialectal_arabic_resources/ --files seg_plus_pos_egy.txt --out test_dar-egy_UPOS.tsv
	python3 convert.py --dir dialectal_arabic_resources/ --files seg_plus_pos_glf.txt --out test_dar-glf_UPOS.tsv
	python3 convert.py --dir dialectal_arabic_resources/ --files seg_plus_pos_lev.txt --out test_dar-lev_UPOS.tsv
	python3 convert.py --dir dialectal_arabic_resources/ --files seg_plus_pos_mgr.txt --out test_dar-mgr_UPOS.tsv

	# Optional checks:
	python3 validate_converted_file.py test_dar-egy_UPOS.tsv tagset_upos.txt
	python3 validate_converted_file.py test_dar-glf_UPOS.tsv tagset_upos.txt
	python3 validate_converted_file.py test_dar-lev_UPOS.tsv tagset_upos.txt
	python3 validate_converted_file.py test_dar-mgr_UPOS.tsv tagset_upos.txt

	cd ..
	mkdir data/pos_tagging
	cp convert-qcri-4dialects/*.tsv data/pos_tagging/
	rm -rf convert-qcri-4dialects


	echo "finnish dialect================================================"
	rm -rf convert-la-murrekorpus
	git clone https://github.com/mainlp/convert-la-murrekorpus.git
	cd convert-la-murrekorpus

	# Retrieve the corpus
	wget https://korp.csc.fi/download/la-murre/vrt/la-murre-vrt.zip
	# unzip la-murre-vrt.zip
	jar -xf la-murre-vrt.zip
	rm la-murre-vrt.zip
	python3 convert.py \
	--outdir "." \
	--groupby "region" \
	--infiles "LA-murre-vrt/lam_*.vrt"

	cd ..
	cp convert-la-murrekorpus/*.tsv data/pos_tagging/
	rm -rf convert-la-murrekorpus

	echo "occitan================================================"
	rm -rf convert-restaure-occitan
	git clone https://github.com/mainlp/convert-restaure-occitan.git
	cd convert-restaure-occitan
	# Get the data
	wget https://zenodo.org/record/1182949/files/CorpusRestaureOccitan.zip
	# unzip CorpusRestaureOccitan.zip
	jar -xf CorpusRestaureOccitan.zip
	rm CorpusRestaureOccitan.zip
	rm -r __MACOSX
	python3 convert.py --glob "CorpusRestaureOccitan/*" --out "test_ROci_UPOS.tsv"
	cd ..
	cp convert-restaure-occitan/*.tsv data/pos_tagging/
	rm -rf convert-restaure-occitan

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
	    --learning_rate 2e-5 \
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
	rm -rf ${result_file}

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

if [[ "$task" = "train_nli" || "$task" = "all" ]]; 
then

	echo "------------------------------Train Dialect NLI------------------------------"
	source vnv/vnv-trns/bin/activate



	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/nli/${lang}"

	python scripts/nli/run_xnli.py \
	  --model_name_or_path ${MODEL_PATH} \
	  --language ${lang} \
	  --train_language ${lang} \
	  --do_train \
	  --dataset_script scripts/nli/dialect_nli.py \
	  --lang_config metadata/nli_metadata.json \
	  --prefix ${lang} \
	  --do_eval \
	  --per_device_train_batch_size 64 \
	  --learning_rate 3e-5 \
	  --num_train_epochs 5.0 \
	  --max_seq_length 128 \
	  --output_dir ${output_dir} \
	  --cache_dir ${CACHE_DIR} \
	  --overwrite_output_dir \
	  --save_total_limit 2 \
	  --save_steps 500 \
	  --eval_steps 500 \
	  --save_strategy="steps" \
	  --evaluation_strategy="steps" \
	  --load_best_model_at_end True
	deactivate
fi

if [[ "$task" = "predict_nli" || "$task" = "all" ]]; 
then

	echo "------------------------------Predict Dialect NLI------------------------------"
	source vnv/vnv-trns/bin/activate

	result_file="${RESULT_FOLDER}/${MODEL_NAME}_${task}_${lang}.txt"
	rm -rf ${result_file}

	output_dir="/scratch/ffaisal/DialectBench/experiments/${MODEL_NAME}/nli/${lang}"

	python scripts/nli/run_xnli.py \
	  --model_name_or_path ${output_dir} \
	  --language ${lang} \
	  --train_language ${lang} \
	  --dataset_script scripts/nli/dialect_nli.py \
	  --lang_config metadata/nli_metadata.json \
	  --result_file ${result_file} \
	  --prefix ${lang} \
	  --do_eval \
	  --do_predict_all \
	  --per_device_train_batch_size 32 \
	  --learning_rate 3e-5 \
	  --num_train_epochs 2.0 \
	  --max_seq_length 128 \
	  --output_dir ${output_dir} \
	  --cache_dir ${CACHE_DIR}
	deactivate
fi

if [[ "$task" = "test" || "$task" = "all" ]]; then

	echo "------------------------------Train Dialect NLI------------------------------"
	source vnv/vnv-trns/bin/activate
	lang="eng_Latn"


	export ALL_lr=("1e-5" "2e-5" "3e-5" "4e-5" "5e-5")
	export ALL_seq=("128")
	export all_batch=("64" "32")
	for lr in ${ALL_lr[@]}; do
		for seq in ${ALL_seq[@]}; do
			for bat in ${all_batch[@]}; do
			output_dir="/scratch/ffaisal/DialectBench/test/${MODEL_NAME}/nli/${lang}-${seq}-${bat}-${lr}"
			python scripts/nli/run_xnli.py \
			  --model_name_or_path ${MODEL_PATH} \
			  --language ${lang} \
			  --train_language ${lang} \
			  --do_train \
			  --dataset_script scripts/nli/dialect_nli.py \
			  --lang_config metadata/nli_metadata.json \
			  --prefix ${lang} \
			  --do_eval \
			  --per_device_train_batch_size ${bat} \
			  --learning_rate ${lr} \
			  --num_train_epochs 5.0 \
			  --max_seq_length ${seq} \
			  --output_dir ${output_dir} \
			  --cache_dir ${CACHE_DIR} \
			  --overwrite_output_dir \
			  --save_total_limit 2 \
			  --save_steps 500 \
			  --eval_steps 500 \
			  --save_strategy="steps" \
			  --evaluation_strategy="steps" \
			  --load_best_model_at_end True \
			  --max_steps 1500
			done
		done
	done
	deactivate

	# export ALL_lr=("1e-5" "2e-5" "3e-5" "4e-5" "5e-5")
	# export ALL_seq=("512" "256" "128")
	# for lr in ${ALL_lr[@]}; do
	# 	for seq in ${ALL_seq[@]}; do
	# 		result_file="/scratch/ffaisal/DialectBench/test//${MODEL_NAME}_sciq_belebele_${lr}_${seq}.txt"
	# 		output_dir="/scratch/ffaisal/DialectBench/test/${MODEL_NAME}/rc/sciq_${dataset}_${lr}_${seq}"
	# 		python scripts/test.py \
	# 		--model_name_or_path ${MODEL_PATH}\
	# 		--do_train \
	# 		--do_eval \
	# 		--do_predict_all \
	# 		--train_file ${train_file} \
	# 		--data_dir ${data_dir} \
	# 		--prefix "train_combined" \
	# 		--learning_rate ${lr} \
	# 		--lang_config metadata/rcmc_metadata.json \
	# 		--num_train_epochs 3 \
	# 		--per_device_eval_batch_size=16 \
	# 		--per_device_train_batch_size=16 \
	# 		--overwrite_output \
	# 		--output_dir ${output_dir} \
	# 		--max_seq_length ${seq} \
	# 		--result_file ${result_file} \
	# 		--cache_dir ${CACHE_DIR} \
	# 		--save_total_limit 2 \
	# 		--save_steps 100 \
	# 		--eval_steps 100 \
	# 		--save_strategy="steps" \
	# 		--evaluation_strategy="steps" \
	# 		--load_best_model_at_end True
	# 	done
	# done

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


# function download_panx {
#     echo "Download panx NER dataset"
#     if [ -f $DIR/AmazonPhotos.zip ]; then
#         base_dir=$DIR/panx_dataset/
#         unzip -qq -j $DIR/AmazonPhotos.zip -d $base_dir
#         cd $base_dir
#         langs=(ar he vi id jv ms tl eu ml ta te af nl en de el bn hi mr ur fa fr it pt es bg ru ja ka ko th sw yo my zh kk tr et fi hu qu pl uk az lt pa gu ro)
#         for lg in ${langs[@]}; do
#             tar xzf $base_dir/${lg}.tar.gz
#             for f in dev test train; do mv $base_dir/$f $base_dir/${lg}-${f}; done
#         done
#         cd ..
#         python $REPO/utils_preprocess.py \
#             --data_dir $base_dir \
#             --output_dir $DIR/panx \
#             --task panx
#         rm -rf $base_dir
#         echo "Successfully downloaded data at $DIR/panx" >> $DIR/download.log
#     else
#         echo "Please download the AmazonPhotos.zip file on Amazon Cloud Drive manually and save it to $DIR/AmazonPhotos.zip"
#         echo "https://www.amazon.com/clouddrive/share/d3KGCRCIYwhKJF0H3eWA26hjg2ZCRhjpEQtDL70FSBN"
#     fi
# }
