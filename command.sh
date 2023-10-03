#!/bin/bash
task=${task:-none}
lang=${lang:-eng}
lang2=${lang2:-eng}
lang3=${lang3:-eng}
MODEL_NAME=${MODEL_NAME:-bert}
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
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model}
		# bash install.sh --task ${task} --lang ${MODEL_NAME} --MODEL_NAME ${base_model}
	done
fi


if [[ "$task" = "train_udp_eng_sing" ]]; then

	#./command.sh --task train_udp_eng_sing --MODEL_NAME bert
	export ALL_MODELS=("UD_English-EWT")
	
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model}
		# bash install.sh --task ${task} --lang ${MODEL_NAME} --MODEL_NAME ${base_model}
	done
fi

if [[ "$task" = "train_udp_eng_TwitterAAE" ]]; then

	#./command.sh --task train_udp_eng_sing --MODEL_NAME bert
	export ALL_MODELS=("UD_English-EWT")
	
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model}
		# bash install.sh --task train_udp_eng_TwitterAAE --lang UD_English-EWT --MODEL_NAME bert
	done
fi

if [[ "$task" = "predict_udp" ]]; then
	efile="tr_output/${base_model}_${task}.err"
	ofile="tr_output/${base_model}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} null ${base_model}
	# bash install.sh --task ${task} --MODEL_NAME ${base_model}

fi

if [[ "$task" = "predict_udp_eng_sing" ]]; then
	#./command.sh --task predict_udp_eng_sing --MODEL_NAME xlmr
	efile="tr_output/${base_model}_${task}.err"
	ofile="tr_output/${base_model}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} null ${base_model}
	# bash install.sh --task ${task} --MODEL_NAME ${base_model}

fi

if [[ "$task" = "predict_udp_eng_TwitterAAE" ]]; then
	#./command.sh --task predict_udp_eng_sing --MODEL_NAME xlmr
	efile="tr_output/${base_model}_${task}.err"
	ofile="tr_output/${base_model}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} null ${base_model}
	# bash install.sh --task predict_udp_eng_TwitterAAE --MODEL_NAME bert

fi