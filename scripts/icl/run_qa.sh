# for lang in "english-irl" "english-kenya" "english-nga" "english-nzl" "english-phl" "english-usa" "english-zaf"
for lang in "arabic-mar" "arabic-dza" "arabic-tun"
do
    echo "Running ${lang}"
    ~/launch-container-ro.sh grok /opt/miniconda/bin/python scripts/icl/eval_qa.py -l ${lang} --gpu-id 0
done