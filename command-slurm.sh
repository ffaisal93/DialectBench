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

if [[ "$task" = "train_sdqa" || "$task" = "predict_sdqa" ]]; then

	export ALL_MODELS=("all" "arabic" "bengali" "english" "finnish" "indonesian" "korean" "russian" "swahili" "telugu")

	# export ALL_MODELS=("UD_English-EWT")
	
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model} dev
		# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model} test
		bash install.sh --task ${task} --lang ${MODEL_NAME} --MODEL_NAME ${base_model} --dataset dev
		bash install.sh --task ${task} --lang ${MODEL_NAME} --MODEL_NAME ${base_model} --dataset test
	done
fi

if [[ "$task" = "translate_nli" ]]; then
	export ALL_TARGETS=("lmo_Latn" "ita_Latn" "fur_Latn" "scn_Latn" "srd_Latn" "vec_Latn" "azb_Arab" "azj_Latn" "tur_Latn" "kmr_Latn" "ckb_Arab" "nno_Latn" "nob_Latn" "lim_Latn" "ltz_Latn" "nld_Latn" "lvs_Latn" "ltg_Latn" "acm_Arab" "acq_Arab" "aeb_Arab" "ajp_Arab" "apc_Arab" "arb_Arab" "ars_Arab" "ary_Arab" "arz_Arab" "kab_Latn" "asm_Beng" "ben_Beng" "lij_Latn" "oci_Latn" "yue_Hant" "zho_Hans" "zho_Hant" "glg_Latn" "spa_Latn" "por_Latn" "nso_Latn" "sot_Latn")

	export ALL_SRC=("ita_Latn" "azj_Latn" "ckb_Arab" "nob_Latn" "nld_Latn" "lvs_Latn" "arb_Arab" "lij_Latn" "zho_Hans" "spa_Latn" "nso_Latn" "ben_Beng")
	
	test_hypo="tempdata/test_hypo-eng_Latn.txt"
	test_premise="tempdata/test_premise-eng_Latn.txt"

	# for TARGET_LANG in "${ALL_TARGETS[@]}"; do
	# 	efile="tr_output/${TARGET_LANG}_${task}-test_hypo.err"
	# 	ofile="tr_output/${TARGET_LANG}_${task}-test_hypo.out"
	# 	echo ${efile}
	# 	echo ${ofile}
	# 	echo ${TARGET_LANG}
	# 	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${TARGET_LANG} test_hypo ${test_hypo}

		# efile="tr_output/${TARGET_LANG}_${task}-test_premise.err"
		# ofile="tr_output/${TARGET_LANG}_${task}-test_premise.out"
		# echo ${efile}
		# echo ${ofile}
		# echo ${TARGET_LANG}
		# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${TARGET_LANG} test_premise ${test_premise}
		# # ./install.sh --task ${task} --lang ${TARGET_LANG} --MODEL_NAME test_hypo --dataset ${test_hypo}
	# done

	# validation_hypo="tempdata/validation_hypo-eng_Latn.txt"
	# validation_premise="tempdata/validation_premise-eng_Latn.txt"
	# for TARGET_LANG in "${ALL_SRC[@]}"; do
	# 	efile="tr_output/${TARGET_LANG}_${task}-validation_hypo.err"
	# 	ofile="tr_output/${TARGET_LANG}_${task}-validation_hypo.out"
	# 	echo ${efile}
	# 	echo ${ofile}
	# 	echo ${TARGET_LANG}
	# 	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${TARGET_LANG} validation_hypo ${validation_hypo}
	# done

	# for TARGET_LANG in "${ALL_SRC[@]}"; do
	# 	efile="tr_output/${TARGET_LANG}_${task}-validation_premise.err"
	# 	ofile="tr_output/${TARGET_LANG}_${task}-validation_premise.out"
	# 	echo ${efile}
	# 	echo ${ofile}
	# 	echo ${TARGET_LANG}
	# 	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${TARGET_LANG} validation_premise ${validation_premise}
	# done

	train_hypo="tempdata/train_hypo-eng_Latn.txt"
	train_premise="tempdata/train_premise-eng_Latn.txt"
	for TARGET_LANG in "${ALL_SRC[@]}"; do
		efile="tr_output/${TARGET_LANG}_${task}-train_premise.err"
		ofile="tr_output/${TARGET_LANG}_${task}-train_premise.out"
		echo ${efile}
		echo ${ofile}
		echo ${TARGET_LANG}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${TARGET_LANG} train_premise ${train_premise}
		
		efile="tr_output/${TARGET_LANG}_${task}-train_hypo.err"
		ofile="tr_output/${TARGET_LANG}_${task}-train_hypo.out"
		echo ${efile}
		echo ${ofile}
		echo ${TARGET_LANG}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${TARGET_LANG} train_hypo ${train_hypo}
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
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model} scripts/ner/norwegian_ner.py
	done

	export ALL_MODELS=("ar" "az" "ku" "tr" "hsb" "nl" "fr" "zh" "en" "mhr" "it" "de" "pa" "es" "hr" "lv" "hi" "ro" "el" "bn")
	##bokmaal:nb, ##nn:nynorsk
	for MODEL_NAME in ${ALL_MODELS[@]}; do
		efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
		ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${MODEL_NAME}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${MODEL_NAME} ${base_model} wikiann
	done
fi

if [[ "$task" = "predict_ner" ]]; 
then
	MODEL_NAME="en"
	efile="tr_output/${base_model}_${MODEL_NAME}_${task}.err"
	ofile="tr_output/${base_model}_${MODEL_NAME}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${predict_ner} ${MODEL_NAME} ${base_model} wikiann
fi

if [[ "$task" = "train_did_lm" || "$task" = "predict_did_lm" ]]; then
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
	echo

fi

# if [[ "$task" = "predict_did_lm" ]]; then
# 	lang="arabic"
# 	dataset="madar"
# 	efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
# 	ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
# 	echo ${efile}
# 	echo ${ofile}
# 	echo ${base_model}
# 	echo ${lang}
# 	echo ${dataset}
# 	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
# 	# ./install.sh --task train_did_lm --lang arabic --dataset madar --MODEL_NAME bert

# fi


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
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
	echo

fi


if [[ "$task" = "train_topic_classification_lm" || "$task" = "predict_topic_classification_lm" ]]; then

	export ALL_LANGS=("eng_Latn" "ita_Latn" "azj_Latn" "ckb_Arab" "nob_Latn" "nld_Latn" "lvs_Latn" "arb_Arab" "lij_Latn" "zho_Hans" "spa_Latn" "nso_Latn")
	dataset="sib"
	for lang in ${ALL_LANGS[@]}; do
		efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
		ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
		echo ${efile}
		echo ${ofile}
		echo ${base_model}
		echo ${lang}
		echo ${dataset}
		sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
		# ./install.sh --task train_topic_classification_lm --lang eng_Latn --dataset sib --MODEL_NAME bert
	done

fi

if [[ "$task" = "train_reading_comprehension" || "$task" = "predict_reading_comprehension" ]]; then

	lang="eng_Latn"
	dataset="Belebele"
	efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
	ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
	echo ${efile}
	echo ${ofile}
	echo ${base_model}
	echo ${lang}
	echo ${dataset}
	sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
	# ./install.sh --task ${task} --lang ${lang} --dataset ${dataset} --MODEL_NAME ${base_model}
	# ./install.sh --task train_reading_comprehension --lang eng_Latn --dataset Belebele --MODEL_NAME bert
		# echo

fi


# if [[ "$task" = "predict_topic_classification_lm" ]]; then
# 	lang="eng_Latn"
# 	dataset="sib"
# 	efile="tr_output/${base_model}_${lang}_${dataset}_${task}.err"
# 	ofile="tr_output/${base_model}_${lang}_${dataset}_${task}.out"
# 	echo ${efile}
# 	echo ${ofile}
# 	echo ${base_model}
# 	echo ${lang}
# 	echo ${dataset}
# 	# sbatch -o ${ofile} -e ${efile} slurm/run_udp.slurm ${task} ${lang} ${base_model} ${dataset}
# 	./install.sh --task predict_topic_classification_lm --lang eng_Latn --dataset sib --MODEL_NAME bert

# fi
