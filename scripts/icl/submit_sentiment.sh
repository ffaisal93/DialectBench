#!/bin/bash
#SBATCH --job-name=dbench-icl-sentiment
#SBATCH --cpus-per-task=1
#SBATCH --mem=32G
#SBATCH --account=argon
#SBATCH --partition=gpu-a40
#SBATCH --time=16:00:00
#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kahuja@uw.edu
#SBATCH --output="slurm_out/slurm-%x-%n-%J.log"

~/launch-container-ro.sh grok /gscratch/argon/kahuja/work/repos/DialectBench/scripts/icl/run_sentiment.sh "arq_arab" "4" "42"