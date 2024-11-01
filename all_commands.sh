#!/bin/bash
action=${action:-none}
execute=${execute:-bash}

while [ $# -gt 0 ]; do

	if [[ $1 == *"--"* ]]; then
		param="${1/--/}"
		declare $param="$2"
		echo $1 $2 #Optional to see the parameter:value result
	fi

	shift
done

if [[ "$execute" = "bash" ]]; then
	script="command-bash.sh"
fi
if [[ "$execute" = "slurm" ]]; then
	script="command-slurm.sh"
fi

##=============================================================================================================
if [[ "$action" = "train_udp" ]]; then

	echo "Dependency parsing training"
	bash ${script} --task train_udp --MODEL_NAME mbert
	bash ${script} --task train_udp --MODEL_NAME xlmr
fi

if [[ "$action" = "predict_udp" ]]; then

	echo "Dependency parsing evaluation"
	bash ${script} --task predict_udp --MODEL_NAME mbert
	bash ${script} --task predict_udp --MODEL_NAME xlmr
	echo

fi
##=============================================================================================================
if [[ "$action" = "train_pos" ]]; then

	echo "training pos tagging"
	bash ${script} --task train_pos --MODEL_NAME mbert
	bash ${script} --task train_pos --MODEL_NAME xlmr
	echo

fi

if [[ "$action" = "predict_pos" ]]; then

	echo "predict pos tagging"
	bash ${script} --task predict_pos --MODEL_NAME mbert
	bash ${script} --task predict_pos --MODEL_NAME xlmr
	echo

fi
##=============================================================================================================
if [[ "$action" = "train_ner" ]]; then

	echo "training named entity recognition"
	bash ${script} --task train_ner --MODEL_NAME mbert
	bash ${script} --task train_ner --MODEL_NAME xlmr
	echo

fi

if [[ "$action" = "predict_ner" ]]; then

	echo "predicting named entity recognition"
	bash ${script} --task predict_ner --MODEL_NAME mbert
	bash ${script} --task predict_ner --MODEL_NAME xlmr
	echo

fi
##=============================================================================================================
if [[ "$action" = "train_topic_classification" ]]; then

	echo "topic classification training using sib data"
	bash ${script} --task train_topic_classification_lm --MODEL_NAME mbert
	bash ${script} --task train_topic_classification_lm --MODEL_NAME xlmr
fi

if [[ "$action" = "predict_topic_classification" ]]; then

	echo "topic classification prediction on sib data"
	bash ${script} --task predict_topic_classification_lm --MODEL_NAME mbert
	bash ${script} --task predict_topic_classification_lm --MODEL_NAME xlmr

fi
##=============================================================================================================
if [[ "$action" = "train_nli" ]]; then

	echo "NLI training"
	bash ${script} --task train_nli --MODEL_NAME mbert
	bash ${script} --task train_nli --MODEL_NAME xlmr
fi

if [[ "$action" = "predict_nli" ]]; then

	echo "NLI prediction"
	bash ${script} --task predict_nli --MODEL_NAME mbert
	bash ${script} --task predict_nli --MODEL_NAME xlmr
fi
##=============================================================================================================
if [[ "$action" = "train_sa" ]]; then

	echo "Sentiment Analysis training"
	bash ${script} --task train_sa --MODEL_NAME mbert
	# bash ${script} --task train_sa --MODEL_NAME xlmr
fi

if [[ "$action" = "predict_sa" ]]; then

	echo "Sentiment Analysis prediction"
	bash ${script} --task predict_sa --MODEL_NAME mbert
	# bash ${script} --task predict_sa --MODEL_NAME xlmr
fi
##=============================================================================================================

if [[ "$action" = "train_did" ]]; then

	echo "dialect identification"
	bash ${script} --task train_did_lm --MODEL_NAME mbert
	bash ${script} --task train_did_lm --MODEL_NAME xlmr
fi

if [[ "$action" = "predict_did" ]]; then

	echo "dialect identification"
	bash ${script} --task predict_did_lm --MODEL_NAME mbert
	bash ${script} --task predict_did_lm --MODEL_NAME xlmr
	bash ${script} --task train_predict_did_ml --MODEL_NAME nb #USING NAIVE-BAYES
fi
##=============================================================================================================

if [[ "$action" = "train_reading_comprehension" ]]; then

	echo "training reading comprehension multiple choice quesiton answering"
	bash ${script} --task train_reading_comprehension --MODEL_NAME mbert
	bash ${script} --task train_reading_comprehension --MODEL_NAME xlmr
	echo

fi

if [[ "$action" = "predict_reading_comprehension" ]]; then

	echo "training reading comprehension multiple choice quesiton answering"
	bash ${script} --task predict_reading_comprehension --MODEL_NAME mbert
	bash ${script} --task predict_reading_comprehension --MODEL_NAME xlmr
	echo

fi
##=============================================================================================================

if [[ "$action" = "predict_sdqa" ]]; then

	echo "predicting SD-QA [extractive quesiton answering]"
	bash ${script} --task predict_sdqa --MODEL_NAME bert
	bash ${script} --task predict_sdqa --MODEL_NAME xlmr
	echo

fi

# ####-------BASH COMMANDS-------#####

### ./all_commands.sh --action train_did --execute slurm # done (madar)
### ./all_commands.sh --action predict_did --execute slurm # done
###	./all_commands.sh --action train_topic_classification --execute slurm # done
###	./all_commands.sh --action predict_topic_classification --execute slurm # done
###	./all_commands.sh --action train_reading_comprehension --execute slurm #done; needs A100 gpu..ow reduce batch size
###	./all_commands.sh --action predict_reading_comprehension --execute slurm #done
###	./all_commands.sh --action predict_sdqa --execute slurm #done

### ./all_commands.sh --action train_ner --execute slurm # done
### ./all_commands.sh --action predict_ner --execute slurm # done

### ./all_commands.sh --action train_nli --execute bash

### ./all_commands.sh --action train_pos --execute bash
### ./all_commands.sh --action predict_pos --execute bash
