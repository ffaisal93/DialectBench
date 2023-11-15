#!/bin/bash
cd /gscratch/argon/kahuja/work/repos/DialectBench
/opt/miniconda/bin/python -m scripts.icl.eval_sentiment -l "$1" -k "$2" -s "$3" --overwrite_cache