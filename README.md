# DialectBench

## Get started

Clone the github repository.

```bash
git clone https://github.com/ffaisal93/DialectBench.io.git
cd DialectBench
```

## Download Data
- Download all data available `[except mt  and the ones loadable through huggingface]`
  ```bash
  bash download_data.sh --task all
  ```
- Download data for Turkish dialectal machine translation
  ```bash
  bash download_data.sh --task machine_translation_turkish
  ```

## Package Installation 
-  `Dependency parsing:` Install Adapter Package
```bash
bash install.sh --task install_adapter
```
- `Extractive Question Answering [SDQA]:` Install Transformers 3.4.0
```bash
bash install.sh --task install_transformers_qa
```
- `Other Structured Prediction, QA and Classification tasks:` Transformers 4.21.1
```bash
bash install.sh --task install_transformers
```

## Task Specific Training and Evaluation

### Dependency Parsing

###### Training

- Finetune all available language-specific models on both pretrained mBERT and XLMR at once
  ```
  ./all_commands.sh --action train_udp --execute bash
  ```
- Finetune one single available language-specific model
  ```
  bash install.sh --task train_udp --lang UD_English-EWT --MODEL_NAME mbert
  ```

###### Prediction
- Prediction on all finetuned model (for both pretrained mBERT and XLMR) and if no training data available for a specific language variety, do zeroshot from English variety `"UD_English-EWT"`
  ```bash
  ./all_commands.sh --action predict_udp --execute bash
  ```
- Do zero-shot prediction from a specific language variety (e.g. `UD_English-EWT`) and on all available variety defined in `--lang_config metadata/udp_metadata.json`
  ```bash
  bash install.sh --task predict_udp_zeroshot_all --lang UD_English-EWT --MODEL_NAME mbert
  ```
- Do test data prediction on a single finetuned language variety (e.g. `UD_English-EWT`)
  ```bash
  bash install.sh --task predict_udp_single --lang UD_English-EWT --MODEL_NAME mbert
  ```

### Parts of Speech (POS) Tagging 

###### Training

- Finetune all available language-specific models on both pretrained mBERT and XLMR at once
  ```
  ./all_commands.sh --action train_pos --execute bash
  ```

###### Prediction
- Prediction on all finetuned model (for both pretrained mBERT and XLMR) and if no training data available for a specific language variety, do zeroshot from English variety `"UD_English-EWT"`
  ```bash
  ./all_commands.sh --action predict_pos --execute bash
  ```

### Named Entity Recognition (NER)

###### Training

- Performing in-variety Finetuning on all available language varieties on both pretrained mBERT and XLMR at one go.
  ```bash
  ./all_commands.sh --action train_pos --execute bash
  ```
- or, If you want to performing in-variety finetuning for a single language only, try the following:
  ```bash
  bash install.sh --task train_ner --lang bokmaal --MODEL_NAME bert --dataset wikiann
  ```
- We have two datasets supported in DialectBench at this point. `wikiann` and `norwegian_ner`.
  - `wikiann`: language varieties `("ar" "az" "ku" "tr" "hsb" "nl" "fr" "zh" "en" "mhr" "it" "de" "pa" "es" "hr" "lv" "hi" "ro" "el" "bn")`. Use `--dataset wikiann` to finetune varieties from this dataset.

  - `norwegian_ner`: language varieties ("bokmaal" "nynorsk" "samnorsk"). Use `--dataset scripts/ner/norwegian_ner.py` to finetune varieties from this dataset.

###### Prediction
- Prediction using all in-variety finetuned models (for both pretrained mBERT and XLMR) as well as performing zeroshot prediction using English variety `en` on the varieties available in `--lang_config metadata/metadata/ner_metadata.json` at one go.
  ```bash
  ./all_commands.sh --action predict_ner --execute bash
  ```


### Topic Classification (TC)

###### Training

- Performing In-cluster finetuning (on both pretrained mbert and xlm-r) on selected varieties from different language cluster.
```bash
./all_commands.sh --action train_topic_classification_lm --execute bash
```
- Add or remove specific variety for finetuning from SIB-200 dataset here in `command-bash.sh` file.
  
  ```bash
      if [[ "$task" = "train_topic_classification_lm" || "$task" = "predict_topic_classification_lm" ]]; then

        export ALL_LANGS=("eng_Latn" "ita_Latn" "azj_Latn" "ckb_Arab" "nob_Latn" "nld_Latn" "lvs_Latn" 
          "arb_Arab" "lij_Latn" "zho_Hans" "spa_Latn" "nso_Latn")

  ``` 

###### Prediction
- Performing inference on all available varieties across different language clusters (as defined in `--lang_config metadata/topic_metadata.json`) and on top of different pretrained models (mbert, xlmr)
```bash
./all_commands.sh --action predict_topic_classification_lm --execute bash
```

### Natural language inference (NLI)

###### Training

- Performing zero-shot finetuning from English (on top of both pretrained mbert and xlm-r) on selected varieties from different language cluster.
```bash
./all_commands.sh --action train_nli --execute bash
```
- Add or remove specific variety for finetuning from translate-test `dialect_nli` dataset here in `command-bash.sh` file.
  
  ```bash
    if [[ "$task" = "train_nli" || "$task" = "predict_nli" ]]; then

      # export ALL_LANGS=("eng_Latn" "ita_Latn" "azj_Latn" "ckb_Arab" "nob_Latn" "nld_Latn" "lvs_Latn" "arb_Arab" "lij_Latn" "zho_Hans" "spa_Latn" "nso_Latn" "ben_Beng")
      export ALL_LANGS=("eng_Latn")
      for lang in "${ALL_LANGS[@]}"; do
        echo ${base_model}
        echo ${lang}
        echo ${dataset}
        bash install.sh --task ${task} --lang ${lang} --MODEL_NAME ${base_model}
      done

    fi
  ``` 
- `dialect_nli` dataset loading script: `--dataset_script scripts/nli/dialect_nli.py`

###### Prediction
- Performing inference on all available varieties across different language clusters (as defined in `--lang_config metadata/nli_metadata.json`) and on top of different pretrained models (mbert, xlmr).
```bash
./all_commands.sh --action predict_nli --execute bash
```


### Sentiment Analysis (SA)

###### Training
- At this point, DialectBench only supports arabic dialectal sentiment analysis. To finetune variety-specific models:
```bash
./all_commands.sh --action train_sa --execute bash
```

###### Prediction
- To evaluate each variety-specific model at one go:
```bash
./all_commands.sh --action predict_sa --execute bash
```
- Add or remove specific variety for finetuning in `command-bash.sh` file.
  
  ```bash
    if [[ "$task" = "train_sa" || "$task" = "predict_sa" ]]; then

      export ALL_LANGS=("aeb_Arab" "aeb_Latn" "arb_arab" "ar-lb" "arq_arab" "ary_arab" "arz_arab" "jor_arab" "sau_arab")
      for lang in "${ALL_LANGS[@]}"; do
        echo ${base_model}
        echo ${lang}
        echo ${dataset}
        bash install.sh --task ${task} --lang ${lang} --lang2 arabic --MODEL_NAME ${base_model}
      done

    fi
  ``` 

### Dialect Identification (DId)

###### Training
- Finetune Arabic, English, Mandarin, Portuguese, Spanish and Swiss-Dialect identification models (mbert and xlmr based)
```bash
./all_commands.sh --action train_did --execute bash
```
- Finetune a dialect identification model of a single language
```bash
export lang="arabic" #"arabic" english" "greek" "mandarin_simplified" "mandarin_traditional" "portuguese" "spanish" "swiss-dialects"
export base_model="mbert" #"mbert" "xlmr"
bash install.sh --task train_did --lang ${lang} --dataset ${dataset} --MODEL_NAME ${base_model}
```

###### Prediction
```bash
./all_commands.sh --action predict_did_lm --execute bash
```

### Machine Reading Comprehension (MRC)

###### Training
```bash
./all_commands.sh --action train_reading_comprehension --execute bash
```

###### Prediction
```bash
./all_commands.sh --action predict_reading_comprehension --execute bash
```

### Extractive Question Answering

###### Training
- Finetune on all language at once as well as on singlae language and it's varieties. 
```bash
./all_commands.sh --action train_sdqa --execute bash
```

- Add or remove specific language cluster in this `command-bash.sh` block.
```bash
f [[ "$task" = "train_sdqa" || "$task" = "predict_sdqa" ]]; then

  export ALL_MODELS=("all" "arabic" "bengali" "english" "finnish" "indonesian" "korean" "russian" "swahili" "telugu")

  for MODEL_NAME in "${ALL_MODELS[@]}"; do
    echo ${base_model}
    echo ${MODEL_NAME}
    bash install.sh --task ${task} --lang ${MODEL_NAME} --MODEL_NAME ${base_model} --dataset dev
    bash install.sh --task ${task} --lang ${MODEL_NAME} --MODEL_NAME ${base_model} --dataset test
  done
fi
```


###### Prediction
```bash
./all_commands.sh --action predict_sdqa --execute bash
```