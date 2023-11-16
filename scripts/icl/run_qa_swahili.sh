for lang in "swahili-kenya" "swahili-tanzania"
do
    echo "Running ${lang}"
    ~/launch-container-ro.sh grok /opt/miniconda/bin/python scripts/icl/eval_qa.py -l ${lang} --gpu-id 1
done