# DialectBench

### installation
comment-out `module load python/3.8.6-ff` inside `install.sh` [specific to GMU cluster]
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
