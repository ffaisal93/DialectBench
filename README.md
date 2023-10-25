# DialectBench

### installation
- Install Adapter Package `[for dependency parsing]`
  ```
  bash install.sh --task install_adapter
  ```
- Install Transformers 3.4.0`[for QA]`
  ```
  bash install.sh --task install_transformers_qa
  ```
- Install Transformers 4.21.1`[for all other tasks]`
  ```
  bash install.sh --task install_transformers_latest
  ```
## Tasks
Basically, start running `all_commands.sh` that calls either `command-bash.sh` or `command-slurm.sh` (through `--execute`; options: [`bash`/`slurm`]) depending on whether you are running bash-script or slurm jobs. Then `command-bash.sh` loops over all the data/model and call `install.sh` to run the training/prediction code snippet.

### Topic-Classification
- Training:
  ```
  ./all_commands.sh --action train_topic_classification --execute bash
  ```
- Prediction:
  ```
  ./all_commands.sh --action predict_topic_classification --execute bash
  ```
