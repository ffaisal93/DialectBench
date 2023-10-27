# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
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

"""The WikiANN dataset for multilingual named entity recognition"""


import os

import datasets


_CITATION = """@inproceedings{pan-etal-2017-cross,
    title = "Cross-lingual Name Tagging and Linking for 282 Languages",
    author = "Pan, Xiaoman  and
      Zhang, Boliang  and
      May, Jonathan  and
      Nothman, Joel  and
      Knight, Kevin  and
      Ji, Heng",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P17-1178",
    doi = "10.18653/v1/P17-1178",
    pages = "1946--1958",
    abstract = "The ambitious goal of this work is to develop a cross-lingual name tagging and linking framework for 282 languages that exist in Wikipedia. Given a document in any of these languages, our framework is able to identify name mentions, assign a coarse-grained or fine-grained type to each mention, and link it to an English Knowledge Base (KB) if it is linkable. We achieve this goal by performing a series of new KB mining methods: generating {``}silver-standard{''} annotations by transferring annotations from English to other languages through cross-lingual links and KB properties, refining annotations through self-training and topic selection, deriving language-specific morphology features from anchor links, and mining word translation pairs from cross-lingual links. Both name tagging and linking results for 282 languages are promising on Wikipedia data and on-Wikipedia data.",
}"""

_DESCRIPTION = """WikiANN (sometimes called PAN-X) is a multilingual named entity recognition dataset consisting of Wikipedia articles annotated with LOC (location), PER (person), and ORG (organisation) tags in the IOB2 format. This version corresponds to the balanced train, dev, and test splits of Rahimi et al. (2019), which supports 176 of the 282 languages from the original WikiANN corpus."""

_DATA_URL = "../data/NER/wikiann_og"
_HOMEPAGE = "../data/NER/test.zip"
_VERSION = "1.1.0"
_LANGS = [
        "kab",
        "kbd",
        "ady",
        "azb",
        "dsb",
        "stq",
        "nrm",
        "jam",
        "koi",
        "kv",
        "mrj",
        "sc",
        "roa-tara",
        "kl",
        "ik",
        "nds-nl",
        "pfl",
        "nso",
        "st",
        "frp",
        "ltg",
        "hif",
        "mo",
        "pnt",
        "roa-rup"
    ]


class WikiannConfig(datasets.BuilderConfig):
    def __init__(self, **kwargs):
        super(WikiannConfig, self).__init__(version=datasets.Version(_VERSION, ""), **kwargs)


class Wikiann(datasets.GeneratorBasedBuilder):
    """WikiANN is a multilingual named entity recognition dataset consisting of Wikipedia articles annotated with LOC, PER, and ORG tags"""

    VERSION = datasets.Version(_VERSION)
    # use two-letter ISO 639-1 language codes as the name for each corpus
    BUILDER_CONFIGS = [
        WikiannConfig(name=lang, description=f"WikiANN NER examples in language {lang}") for lang in _LANGS
    ]

    def _tags_to_spans(self, tags):
        """Convert tags to spans."""
        spans = set()
        span_start = 0
        span_end = 0
        active_conll_tag = None
        for index, string_tag in enumerate(tags):
            # Actual BIO tag.
            bio_tag = string_tag[0]
            assert bio_tag in ["B", "I", "O"], "Invalid Tag"
            conll_tag = string_tag[2:]
            if bio_tag == "O":
                # The span has ended.
                if active_conll_tag:
                    spans.add((active_conll_tag, (span_start, span_end)))
                active_conll_tag = None
                # We don't care about tags we are
                # told to ignore, so we do nothing.
                continue
            elif bio_tag == "B":
                # We are entering a new span; reset indices and active tag to new span.
                if active_conll_tag:
                    spans.add((active_conll_tag, (span_start, span_end)))
                active_conll_tag = conll_tag
                span_start = index
                span_end = index
            elif bio_tag == "I" and conll_tag == active_conll_tag:
                # We're inside a span.
                span_end += 1
            else:
                # This is the case the bio label is an "I", but either:
                # 1) the span hasn't started - i.e. an ill formed span.
                # 2) We have IOB1 tagging scheme.
                # We'll process the previous span if it exists, but also include this
                # span. This is important, because otherwise, a model may get a perfect
                # F1 score whilst still including false positive ill-formed spans.
                if active_conll_tag:
                    spans.add((active_conll_tag, (span_start, span_end)))
                active_conll_tag = conll_tag
                span_start = index
                span_end = index
        # Last token might have been a part of a valid span.
        if active_conll_tag:
            spans.add((active_conll_tag, (span_start, span_end)))
        # Return sorted list of spans
        return sorted(list(spans), key=lambda x: x[1][0])

    def _get_spans(self, tokens, tags):
        """Convert tags to textspans."""
        spans = self._tags_to_spans(tags)
        text_spans = [x[0] + ": " + " ".join([tokens[i] for i in range(x[1][0], x[1][1] + 1)]) for x in spans]
        if not text_spans:
            text_spans = ["None"]
        return text_spans

    def _info(self):
        features = datasets.Features(
            {
                "tokens": datasets.Sequence(datasets.Value("string")),
                "ner_tags": datasets.Sequence(
                    datasets.features.ClassLabel(
                        names=[
                            "O",
                            "B-PER",
                            "I-PER",
                            "B-ORG",
                            "I-ORG",
                            "B-LOC",
                            "I-LOC",
                        ]
                    )
                ),
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        # wikiann_dl_dir = dl_manager.download_and_extract(_DATA_URL)
        wikiann_dl_dir=_DATA_URL
        lang = self.config.name
        lang_archive = os.path.join(wikiann_dl_dir, lang + ".tar.gz")
        print(dl_manager.iter_archive(lang_archive))

        return [
            # datasets.SplitGenerator(
            #     name=datasets.Split.VALIDATION,
            #     gen_kwargs={"filepath": "dev", "files": dl_manager.iter_archive(lang_archive)},
            # ),
            # datasets.SplitGenerator(
            #     name=datasets.Split.TEST,
            #     gen_kwargs={"filepath": "test", "files": dl_manager.iter_archive(lang_archive)},
            # ),
            # datasets.SplitGenerator(
            #     name=datasets.Split.TRAIN,
            #     gen_kwargs={"filepath": "train", "files": dl_manager.iter_archive(lang_archive)},
            # ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={"filepath": "wikiann-{}.bio".format(lang), "files": dl_manager.iter_archive(lang_archive)},
            ),
        ]

    def _generate_examples(self, filepath, files):
        """Reads line by line format of the NER dataset and generates examples.
        Input Format:
        en:rick  B-PER
        en:and  O
        en:morty  B-PER
        en:are  O
        en:cool  O
        en:.  O
        Output Format:
        {
        'tokens': ["rick", "and", "morty", "are", "cool", "."],
        'ner_tags': ["B-PER", "O" , "B-PER", "O", "O", "O"],
        'langs': ["en", "en", "en", "en", "en", "en"]
        'spans': ["PER: rick", "PER: morty"]
        }
        Args:
            filepath: Path to file with line by line NER format.
        Returns:
            Examples with the format listed above.
        """
        guid_index = 1

        for path, f in files:
            if path == filepath:
                tokens = []
                ner_tags = []
                langs = []
                for line in f:
                    line = line.decode("utf-8")
                    if line == "" or line == "\n":
                        if tokens:
                            # spans = self._get_spans(tokens, ner_tags)
                            yield guid_index, {"tokens": tokens, "ner_tags": ner_tags}
                            guid_index += 1
                            tokens = []
                            ner_tags = []
                            langs = []
                    else:
                        # wikiann data is tab separated
                        splits = line.strip().split(' ')
                        # strip out en: prefix
                        # langs.append(splits[0].split(":")[0])
                        tokens.append(splits[0].strip())
                        if len(splits) > 1:
                            ner_tags.append(splits[-1].replace("\n", ""))
                        else:
                            # examples have no label in test set
                            ner_tags.append("O")
                break