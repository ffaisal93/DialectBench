for lang in "bengali-dhaka" "bengali-ind"
do
    echo "Running ${lang}"
    ~/launch-container-ro.sh grok /opt/miniconda/bin/python scripts/icl/eval_qa.py -l ${lang} --gpu-id 0
done