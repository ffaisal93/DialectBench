#!/bin/bash
#SBATCH --partition=gpuq                    # the DGX only belongs in the 'gpu'  partition
#SBATCH --qos=gpu                           # need to select 'gpu' QoS
#SBATCH --job-name=python-gpu
##SBATCH --output=../tr_output/udp_all.out
##SBATCH --error=../tr_output/udp_all.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1                 # up to 128; 
#SBATCH --gres=gpu:A100.80gb:1              # up to 8; only request what you need
#SBATCH --mem-per-cpu=90G                 # memory per CORE; total memory is 1 TB (1,000,000 MB)
#SBATCH --export=ALL 
#SBATCH --time=3-01:00:00                   # set to 1hr; please choose carefully


task=$1
lang=$2
MODEL_NAME=$3
DATASET=$4

# to see ID and state of GPUs assigned
nvidia-smi
echo ${task} ${lang} ${MODEL_NAME}
pwd

if [[ "$task" = "train_udp" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME}
fi

if [[ "$task" = "predict_udp" ]]; then
	bash install.sh --task ${task} --MODEL_NAME ${MODEL_NAME}
fi

if [[ "$task" = "train_sdqa" || "$task" = "predict_sdqa" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi

if [[ "$task" = "train_ner" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi

if [[ "$task" = "predict_ner" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi


if [[ "$task" = "train_did_lm" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi

if [[ "$task" = "predict_did_lm" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi

if [[ "$task" = "train_predict_did_ml" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi



if [[ "$task" = "train_topic_classification_lm" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi

if [[ "$task" = "predict_topic_classification_lm" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi



if [[ "$task" = "train_reading_comprehension" || "$task" = "predict_reading_comprehension" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi


if [[ "$task" = "translate_nli" ]]; then
	bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${MODEL_NAME} --dataset ${DATASET}
fi
