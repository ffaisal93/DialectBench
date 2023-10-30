# coding=utf-8
# Copyright 2020 HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""MasakhaNER: Named Entity Recognition for African Languages"""

import datasets
import os

logger = datasets.logging.get_logger(__name__)


_CITATION = """\
@article{Adelani2021MasakhaNERNE,
  title={MasakhaNER: Named Entity Recognition for African Languages},
  author={D. Adelani and Jade Abbott and Graham Neubig and Daniel D'Souza and Julia Kreutzer and Constantine Lignos
  and Chester Palen-Michel and Happy Buzaaba and Shruti Rijhwani and Sebastian Ruder and Stephen Mayhew and
  Israel Abebe Azime and S. Muhammad and Chris C. Emezue and Joyce Nakatumba-Nabende and Perez Ogayo and
  Anuoluwapo Aremu and Catherine Gitau and Derguene Mbaye and J. Alabi and Seid Muhie Yimam and Tajuddeen R. Gwadabe and
  Ignatius Ezeani and Rubungo Andre Niyongabo and Jonathan Mukiibi and V. Otiende and Iroro Orife and Davis David and
  Samba Ngom and Tosin P. Adewumi and Paul Rayson and Mofetoluwa Adeyemi and Gerald Muriuki and Emmanuel Anebi and
  C. Chukwuneke and N. Odu and Eric Peter Wairagala and S. Oyerinde and Clemencia Siro and Tobius Saul Bateesa and
  Temilola Oloyede and Yvonne Wambui and Victor Akinode and Deborah Nabagereka and Maurice Katusiime and
  Ayodele Awokoya and Mouhamadane Mboup and D. Gebreyohannes and Henok Tilaye and Kelechi Nwaike and Degaga Wolde and
   Abdoulaye Faye and Blessing Sibanda and Orevaoghene Ahia and Bonaventure F. P. Dossou and Kelechi Ogueji and
   Thierno Ibrahima Diop and A. Diallo and Adewale Akinfaderin and T. Marengereke and Salomey Osei},
  journal={ArXiv},
  year={2021},
  volume={abs/2103.11811}
}
"""

_DESCRIPTION = """\
MasakhaNER is the first large publicly available high-quality dataset for named entity recognition (NER) in ten African languages.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example:
[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .
MasakhaNER is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for ten African languages:
- Amharic
- Hausa
- Igbo
- Kinyarwanda
- Luganda
- Luo
- Nigerian-Pidgin
- Swahili
- Wolof
- Yoruba

The train/validation/test sets are available for all the ten languages.

For more details see https://arxiv.org/abs/2103.11811
"""

_URL = "https://github.com/masakhane-io/masakhane-ner/raw/main/data/"
_TRAINING_FILE = "train.txt"
_DEV_FILE = "dev.txt"
_TEST_FILE = "test.txt"

_DATA_DIR = "../data/pos_tagging"

_LANGUAGES = ("dar-egy","dar-glf", "dar-lev", "dar-mgr","murre-HÄM","murre-KAA", "murre-LOU",
    "murre-LVÄ","murre-POH","murre-SAV","ROci")

class MasakhanerConfig(datasets.BuilderConfig):
    """BuilderConfig for Masakhaner"""

    def __init__(self, language: str,**kwargs):
        """BuilderConfig for Masakhaner.

        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(MasakhanerConfig, self).__init__(**kwargs)
        self.language = language


class Masakhaner(datasets.GeneratorBasedBuilder):
    """Masakhaner dataset."""

    BUILDER_CONFIGS = [
        MasakhanerConfig(
            name=lang,
            language=lang,
            version=datasets.Version("1.1.0", ""),
            description=f"Plain text import of XNLI for the {lang} language",
        )
        for lang in _LANGUAGES
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "upos": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "NOUN",
                                "PUNCT",
                                "ADP",
                                "NUM",
                                "SYM",
                                "SCONJ",
                                "ADJ",
                                "PART",
                                "DET",
                                "CCONJ",
                                "PROPN",
                                "PRON",
                                "X",
                                "_",
                                "ADV",
                                "INTJ",
                                "VERB",
                                "AUX",
                                "CONJ",
                                "root"
                            ]
                        )
                    ),
                }
            ),
            supervised_keys=None,
            homepage="https://arxiv.org/abs/2103.11811",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        urls_to_download = {
            "test": f"{_DATA_DIR}",
        }

        return [
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": os.path.join(self.config.data_dir,'test_{}_UPOS.tsv'.format(self.config.name))}),
        ]

    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            guid = 0
            tokens = []
            upos = []
            for line in f:
                if line == "" or line == "\n":
                    if tokens:
                        yield guid, {
                            "id": str(guid),
                            "tokens": tokens,
                            "upos": upos,
                        }
                        guid += 1
                        tokens = []
                        upos = []
                else:
                    # Masakhaner tokens are space separated
                    splits = line.split("\t")
                    tokens.append(splits[0])
                    upos.append(splits[1].rstrip())
            # last example
            if tokens:
                yield guid, {
                    "id": str(guid),
                    "tokens": tokens,
                    "upos": upos,
                }