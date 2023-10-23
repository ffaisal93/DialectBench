#!/bin/bash
task=${task:-none}
lang=${lang:-eng}
lang2=${lang2:-eng}
lang3=${lang3:-eng}
MODEL_NAME=${MODEL_NAME:-bert}
dataset=${dataset:-wikiann}

while [ $# -gt 0 ]; do

   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
        echo $1 $2 #Optional to see the parameter:value result
   fi

  shift
done

declare -a base_models=("bert" "xlmr")
if [[ "$MODEL_NAME" = "bert" ]]; then
		base_model=${base_models[0]}
fi

if [[ "$MODEL_NAME" = "xlmr" ]]; then
	base_model=${base_models[1]}
fi

if [[ "$task" = "train_udp" ]]; then

	export ALL_MODELS=("UD_Armenian-ArmTDP" "UD_Norwegian-Nynorsk" "UD_Portuguese-Bosque" "UD_Italian-PoSTWITA" "UD_Old_French-SRCMF" "UD_North_Sami-Giella" "UD_Norwegian-Bokmaal" "UD_French-ParisStories" "UD_Italian-MarkIT" "UD_Chinese-GSDSimp" "UD_English-EWT" "UD_French-Rhapsodie" "UD_French-ParTUT" "UD_Classical_Chinese-Kyoto" "UD_Norwegian-NynorskLIA" "UD_Arabic-NYUAD" "UD_Portuguese-PetroGold" "UD_Italian-TWITTIRO" "UD_Turkish_German-SAGT" "UD_Maghrebi_Arabic_French-Arabizi" "UD_Portuguese-CINTIL" "UD_Ligurian-GLT" "UD_Dutch-Alpino" "UD_Western_Armenian-ArmTDP" "UD_Portuguese-GSD" "singlish" "UD_Arabic-PADT")

	# export ALL_MODELS=("UD_English-EWT")
	
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model}
		bash install.sh --task train_udp --lang ${MODEL_NAME} --MODEL_NAME ${base_model}
		# bash install.sh --task train_udp --lang UD_English-EWT --MODEL_NAME xlmr
	done
fi


if [[ "$task" = "predict_udp" ]]; then
	efile="tr_output/${base_model}_${task}.err"
	ofile="tr_output/${base_model}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} null ${base_model}
	#./command.sh --task predict_udp --MODEL_NAME bert
	# bash install.sh --task ${task} --MODEL_NAME ${base_model}

fi

if [[ "$task" = "train_sdqa" ]]; then

	export ALL_MODELS=("all" "arabic" "bengali" "english" "finnish" "indonesian" "korean" "russian" "swahili" "telugu")

	# export ALL_MODELS=("UD_English-EWT")
	
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model}
		# bash install.sh --task train_sdqa --lang ${MODEL_NAME} --MODEL_NAME ${base_model}
		# bash install.sh --task train_udp --lang UD_English-EWT --MODEL_NAME xlmr
	done
fi

if [[ "$task" = "train_ner" ]]; then

	
	###norwegian dialects
	export ALL_MODELS=("bokmaal" "nynorsk" "samnorsk")
	##bokmaal:nb, ##nn:nynorsk
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model} scripts/ner/norwegian_ner.py
		# bash install.sh --task train_ner --lang ${MODEL_NAME} --MODEL_NAME ${base_model} --dataset scripts/ner/norwegian_ner.py
		# bash install.sh --task train_ner --lang bokmaal --MODEL_NAME bert
	done

	export ALL_MODELS=("ar" "ady" "az" "ku" "tr" "dsb" "nl" "fr" "zh" "en" "kv" "mhr" "it" "de" "pa" "es" "hr" "lij" "lv" "hi" "ro" "el")
	export ALL_MODELS=("mhr" "it" "de" "pa" "es" "hr" "lij" "lv" "hi" "ro" "el")
	##bokmaal:nb, ##nn:nynorsk
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model} wikiann
		# bash install.sh --task train_ner --lang ${MODEL_NAME} --MODEL_NAME ${base_model} --dataset wikiann
		# bash install.sh --task train_ner --lang bokmaal --MODEL_NAME bert --dataset wikiann
	done
fi

if [[ "$task" = "train_did_lm" ]]; then
	lang="arabic"
	dataset="madar"
	efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
	ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	echo ${lang}
	echo ${dataset}
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
	# ./install.sh --task train_did_lm --lang arabic --dataset madar --MODEL_NAME bert

fi

if [[ "$task" = "train_predict_did_ml" ]]; then
	lang="arabic"
	dataset="madar"
	efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
	ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	echo ${lang}
	echo ${dataset}
	# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
	./install.sh --task train_predict_did_ml --lang arabic --dataset madar --MODEL_NAME nb

fi

if [[ "$task" = "train_topic_classification_lm" ]]; then
	lang="eng_Latn"
	dataset="sib"
	efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
	ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	echo ${lang}
	echo ${dataset}
	# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
	./install.sh --task train_topic_classification_lm --lang eng_Latn --dataset sib --MODEL_NAME bert

fi

if [[ "$task" = "predict_topic_classification_lm" ]]; then
	lang="eng_Latn"
	dataset="sib"
	efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
	ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	echo ${lang}
	echo ${dataset}
	# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
	./install.sh --task predict_topic_classification_lm --lang eng_Latn --dataset sib --MODEL_NAME bert

fi
