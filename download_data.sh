#!/bin/bash
task=${task:-none}
action=${action:-bash}

ROOT_DIR="$PWD"



while [ $# -gt 0 ]; do

   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
        echo $1 $2 #Optional to see the parameter:value result
   fi

  shift
done


if [[ "$action" = "cluster" ]]; then
   module load git
   module load zip
   module load openjdk/11.0.2-qg

fi

function mkdir_if_not_exists() {
  local dir="$1"
  
  if [ ! -d "$dir" ]; then
    mkdir "$dir"
  fi
}



download_unzip_rename() {

  local url=$1
  local dirname=$2

  cd "$dirname"
  echo $PWD
  local zipname=$(basename "$url")

  wget -O "$zipname" "$url"

  if [[ "$action" = "cluster" ]]; 
  then
   jar -xf "$zipname"
  fi

  if [[ "$action" = "bash" ]]; 
  then
   unzip "$zipname" -x __MACOSX/*

   local extracted=$(unzip -l "$zipname" | awk '/ extracting: /{print $2}')
  fi
  
  rm "$zipname"
  find . -type d -name '__MACOSX*' -prune -exec rm -rf {} +
  find . -type d -name '.DS_Store*' -prune -exec rm -rf {} +
  find . -type d -name '._*' -prune -exec rm -rf {} +
}

# Set directory name 
DATA_DIR="data" 

# Prepend current working directory 
DATA_DIR="$PWD/$DATA_DIR"
mkdir_if_not_exists "$DATA_DIR"


if [[ "$task" = "sib-200" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/ERScX_B9fu5Hq3Fj5Pq333UBewggAh6muCn6-2QFwXzBTw?download=1"
   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "sdqa-gold" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/Edn_aH0aNXNDk_1sb8AVjoQBjcEC_UV0WgvYC0i1T6qPEA?download=1"
   QA_DIR="${DATA_DIR}/Question-Answering"
   mkdir_if_not_exists "$QA_DIR"
   download_unzip_rename $URL $QA_DIR
   cd "$ROOT_DIR"
fi

if [[ "$task" = "ner" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EcwcH77QqiZEi65PLVUlaKIBNe5QR5p9HMUf0D_2FlUgNQ?download=1"
   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "pos_tagging" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EezOARGyNFBMuCoh153s9zMBf3Xshu74lGNJvr4eYp9kNQ?download=1"
   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "parsing" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EcHXqHjT0dhBuRsPhWOL8DwBAUFchNPIggeXuZkFe3V4ng?download=1"
   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "sentiment_analysis" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EdGO7s9qZwBMuX91CBKInqABNm1PilX04ljZKjJjdMbwuA?download=1"
   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "dialect_identification" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EcVynGbCzlZFjMFCIeX9IEsBYRk4WUsvdXAR0WiOaO-rgw?download=1"

   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "reading_comprehension" || "$task" = "all" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EYoMQFLoc2pDiP50TPD3zm0B9bhRWLlZh6vf6rTgu2PJUg?download=1"

   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "machine_translation_turkish" ]]; 
then

   URL="https://gmuedu-my.sharepoint.com/:u:/g/personal/ffaisal_gmu_edu/EbUIQno-MQtLkZ4BH5Z5CisBtBMWXua-PJcOLjWJr_QS8g?download=1"

   download_unzip_rename $URL data
   cd "$ROOT_DIR"
fi

if [[ "$task" = "sentiment_analysis_raw" ]]; 
then
   SA_DIR="${DATA_DIR}/sentiment_analysis"
   rm -rf "${SA_DIR}"
   mkdir_if_not_exists "$SA_DIR"
   mkdir_if_not_exists "$SA_DIR/arabic"
   SA_DIR="$SA_DIR/arabic"
   pip install openpyxl
   
   #TSAC
   #tunisian arabic: https://github.com/fbougares/TSAC
   # Salima Medhaffar, Fethi Bougares, Yannick Estève and Lamia Hadrich-Belguith. Sentiment analysis of Tunisian dialects: Linguistic Ressources and Experiments. WANLP 2017. EACL 2017
   git clone https://github.com/fbougares/TSAC.git
   python scripts/process_dataset.py --dataset TSAC --datapath "$SA_DIR"
   rm -rf TSAC

   #TUNIZI
   #https://github.com/iCompass-ai/TUNIZI/tree/main
   #https://www.aclweb.org/anthology/2021.wanlp-1.25.pdf
   git clone https://github.com/iCompass-ai/TUNIZI.git
   python scripts/process_dataset.py --dataset TUNIZI --datapath "$SA_DIR"
   rm -rf TUNIZI

   # Algerian
   # @INPROCEEDINGS{9068897, author={A. {Abdelli} and F. {Guerrouf} and O. {Tibermacine} and B. {Abdelli}}, booktitle={2019 International Conference on Intelligent Systems and Advanced Computing Sciences (ISACS)}, title={Sentiment Analysis of Arabic Algerian Dialect Using a Supervised Method}, year={2019}, volume={}, number={}, pages={1-6},}
   git clone https://github.com/adelabdelli/DzSentiA.git
   python scripts/process_dataset.py --dataset DzSentiA --datapath "$SA_DIR"
   rm -rf DzSentiA

   ## saudi
   # @inproceedings{[Alqahtani et al., 2022],
   #   title={Customer Sentiments Toward Saudi Banks During the Covid-19 Pandemic},
   #   author={Dhuha Alqahtani, Lama Alzahrani, Maram Bahareth, Nora Alshameri, Hend Al-Khalifa and Luluh Aldhubayi},
   #   booktitle={Soon},
   #   year={2022}
   # }
   git clone https://github.com/iwan-rg/Saudi-Bank-Sentiment-Dataset.git
   python scripts/process_dataset.py --dataset Saudi-Bank-Sentiment-Dataset --datapath "$SA_DIR"
   rm -rf Saudi-Bank-Sentiment-Dataset

   # ## moroccan arabic,MSA
   # @InProceedings{Garouani_MAC,
   # author="Garouani, Moncef
   # and Kharroubi, Jamal",
   # title="MAC: An Open and Free Moroccan Arabic Corpus for Sentiment Analysis",
   # booktitle="Innovations in Smart Cities Applications Volume 5",
   # year="2022",
   # publisher="Springer International Publishing",
   # address="Cham",
   # pages="849--858",
   # doi="10.1007/978-3-030-94191-8_68"
   # }
   git clone https://github.com/LeMGarouani/MAC.git
   python scripts/process_dataset.py --dataset MAC --datapath "$SA_DIR"
   rm -rf MAC

   #egyptian-arabic
   #https://github.com/mahmoudnabil/ASTD/tree/master
   # ASTD: Arabic Sentiment Tweets Dataset
   # Mahmoud Nabil, Mohamed Aly, Amir Atiya
   git clone https://github.com/mahmoudnabil/ASTD.git
   python scripts/process_dataset.py --dataset ASTD --datapath "$SA_DIR"
   rm -rf ASTD

   #jordan-arabic
   # Arabic Tweets Sentimental Analysis Using Machine Learning
   # Khaled Mohammad Alomari, Hatem M. ElSherif & Khaled Shaalan 
   git clone https://github.com/komari6/Arabic-twitter-corpus-AJGT.git
   python scripts/process_dataset.py --dataset Arabic-twitter-corpus-AJGT --datapath "$SA_DIR"
   rm -rf Arabic-twitter-corpus-AJGT

   ##lebanese-arabic
   # @misc{Dua:2019 ,
   # author = "Dua, Dheeru and Graff, Casey",
   # year = "2017",
   # title = "{UCI} Machine Learning Repository",
   # url = "http://archive.ics.uci.edu/ml",
   # institution = "University of California, Irvine, School of Information and Computer Sciences" }
   # @InProceedings{AlOmari2019oclar,
   # title = {Sentiment Classifier: Logistic Regression for Arabic Services Reviews in Lebanon},
   # authors={Al Omari, M., Al-Hajj, M., Hammami, N., & Sabra, A.},
   # year={2019}
   # }
   python scripts/process_dataset.py --dataset oclar --datapath "$SA_DIR"


fi

if [[ "$task" = "dialect_identification_raw" ]]; 
then
   SA_DIR="${DATA_DIR}/dialect-identification"
   mkdir_if_not_exists "$SA_DIR"
   
   ###greek
   mkdir_if_not_exists "$SA_DIR/greek"
   SA_DIR="$SA_DIR/greek"
   #Cypriot Greek (CG) or Standard Modern Greek (SMG)
   git clone https://github.com/hb20007/greek-dialect-classifier.git
   python scripts/process_dataset.py --dataset greek-dialect-classifier --datapath "$SA_DIR"
   rm -rf greek-dialect-classifier

   ##portougese, spanish, english
   git clone https://github.com/LanguageTechnologyLab/DSL-TL.git
   python scripts/process_dataset.py --dataset DSL-TL --datapath DSL-TL
   mkdir_if_not_exists "$SA_DIR/english"
   mv DSL-TL/english-train.csv "$SA_DIR/english/train.csv"
   mv DSL-TL/english-dev.csv "$SA_DIR/english/dev.csv"
   mkdir_if_not_exists "$SA_DIR/spanish"
   mv DSL-TL/spanish-train.csv "$SA_DIR/spanish/train.csv"
   mv DSL-TL/spanish-dev.csv "$SA_DIR/spanish/dev.csv"
   mkdir_if_not_exists "$SA_DIR/portuguese"
   cp DSL-TL/portuguese* "$SA_DIR/portuguese"
   mv DSL-TL/portuguese-train.csv "$SA_DIR/portuguese/train.csv"
   mv DSL-TL/portuguese-dev.csv "$SA_DIR/portuguese/dev.csv"
   rm -rf DSL-TL

   ##swiss-dialect
   mkdir_if_not_exists "$SA_DIR/swiss-dialects"
   python scripts/process_dataset.py --dataset "statworx/swiss-dialects" --datapath "$SA_DIR/swiss-dialects"

   ##mainland, taiwan variation of mandarin
   git clone https://github.com/AlexYangLi/DMT.git
   mkdir_if_not_exists "$SA_DIR/mandarin_simplified"
   mkdir_if_not_exists "$SA_DIR/mandarin_traditional"
   python scripts/process_dataset.py --dataset "DMT" --datapath "DMT"
   mv DMT/mandarin_simplified-train.csv "$SA_DIR/mandarin_simplified/train.csv"
   mv DMT/mandarin_simplified-dev.csv "$SA_DIR/mandarin_simplified/dev.csv"
   mv DMT/mandarin_traditional-train.csv "$SA_DIR/mandarin_traditional/train.csv"
   mv DMT/mandarin_traditional-dev.csv "$SA_DIR/mandarin_traditional/dev.csv"
   rm -rf DMT



fi


## ./download_data.sh --task sib-200
