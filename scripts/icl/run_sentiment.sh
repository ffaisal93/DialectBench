#!/bin/bash
cd /gscratch/argon/kahuja/work/repos/DialectBench
/opt/miniconda/bin/python -m scripts.icl.eval_sentiment -l "$1" -k "$2" -s "$3" --overwrite_cache

# ~/launch-container-ro.sh grok /opt/miniconda/bin/python -m scripts.icl.eval_sentiment -l arq_arab -k 4 -s 42 --overwrite_cache