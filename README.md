# DialectBench

### download_data
- Download all data available [except mt  and the ones loadable through huggingface]
  ```
  bash download_data.sh --task all
  ```
- Download Turkish dialectal machine translations
  ```
  bash download_data.sh --task machine_translation_turkish
  ```
## Task Specific Training and Evaluation

### Dependency Parsing
- Install Adapter Package `[for dependency parsing]`
  ```
  bash install.sh --task install_adapter
  ```
- Finetune all available language-specific models on pretrained mBERT and XLMR at once
  ```
  ./all_commands.sh --action train_udp --execute bash
  ```
- Finetune one single available language-specific model
  ```
  bash install.sh --task train_udp --lang UD_English-EWT --MODEL_NAME mbert
  ```

### installation
comment-out `module load python/3.8.6-ff` inside `install.sh` [specific to cluster]
- Install Adapter Package `[for dependency parsing]`
  ```
  bash install.sh --task install_adapter
  ```
- Install Transformers 3.4.0 `[for QA]`
  ```
  bash install.sh --task install_transformers_qa
  ```
- Install Transformers 4.21.1 `[for all other tasks]`
  ```
  bash install.sh --task install_transformers
  ```
## Tasks
Basically, start running `all_commands.sh` that calls either `command-bash.sh` or `command-slurm.sh` (through `--execute`; options: [`bash`/`slurm`]) depending on whether you are running bash-script or slurm jobs. Then `command-bash.sh` loops over all the data/model and call `install.sh` to run the training/prediction code snippet.

### Topic-Classification
- get the sib-200 data:
  ```
  bash install --task create_sib_topic_classification
  ```
- Training:
  ```
  ./all_commands.sh --action train_topic_classification --execute bash
  ```
- Prediction:
  ```
  ./all_commands.sh --action predict_topic_classification --execute bash
  ```
