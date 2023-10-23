#!/bin/bash
action=${action:-none}

while [ $# -gt 0 ]; do

   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
        echo $1 $2 #Optional to see the parameter:value result
   fi

  shift
done



if [[ "$action" = "train_did" ]]; then

	echo "dialect identification: (only madar at this point)"
	./command-slurm.sh --task train_did_lm --MODEL_NAME bert
	./command-slurm.sh --task train_did_lm --MODEL_NAME xlmr
fi

if [[ "$action" = "predict_did" ]]; then

	echo "dialect identification: (only madar at this point)"
	./command-slurm.sh --task predict_did_lm --MODEL_NAME bert
	./command-slurm.sh --task predict_did_lm --MODEL_NAME xlmr
	./command-slurm.sh --task train_predict_did_ml --MODEL_NAME nb #USING NAIVE-BAYES
fi



if [[ "$action" = "train_topic_classification" ]]; then

	echo "topic classification training using sib data"
	./command-slurm.sh --task train_topic_classification_lm --MODEL_NAME bert
	./command-slurm.sh --task train_topic_classification_lm --MODEL_NAME xlmr
fi

if [[ "$action" = "predict_topic_classification" ]]; then

	echo "topic classification prediction on sib data"
	./command-slurm.sh --task predict_topic_classification_lm --MODEL_NAME bert
	./command-slurm.sh --task predict_topic_classification_lm --MODEL_NAME xlmr

fi



if [[ "$action" = "train_reading_comprehension" ]]; then

	echo "training reading comprehension multiple choice quesiton answering"
	./command-slurm.sh --task train_reading_comprehension --MODEL_NAME bert
	./command-slurm.sh --task train_reading_comprehension --MODEL_NAME xlmr
	echo

fi

if [[ "$action" = "predict_reading_comprehension" ]]; then

	echo "training reading comprehension multiple choice quesiton answering"
	./command-slurm.sh --task predict_reading_comprehension --MODEL_NAME bert
	./command-slurm.sh --task predict_reading_comprehension --MODEL_NAME xlmr
	echo

fi



if [[ "$action" = "predict_sdqa" ]]; then

	echo "predicting SD-QA [extractive quesiton answering]"
	./command-slurm.sh --task predict_sdqa --MODEL_NAME bert
	./command-slurm.sh --task predict_sdqa --MODEL_NAME xlmr
	echo

fi




# ####-------BASH COMMANDS-------#####




### ./all_commands.sh --action train_did # done (madar)
### ./all_commands.sh --action predict_did # done
###	./all_commands.sh --action train_topic_classification # done
###	./all_commands.sh --action predict_topic_classification # done
###	./all_commands.sh --action train_reading_comprehension #done; needs A100 gpu..ow reduce batch size
###	./all_commands.sh --action predict_reading_comprehension #done
###	./all_commands.sh --action predict_sdqa #done
