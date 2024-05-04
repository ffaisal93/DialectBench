INSTRUCTIONS = {
    "nli": """Instruction: Given a premise and a hypothesis, determine the relationship between them. The possible relationships are:
- Entailment: The hypothesis follows logically from the premise.
- Neutral: The hypothesis may or may not be true given the premise.
- Contradiction: The hypothesis contradicts or is inconsistent with the premise.
""",

    "xquad": "You are an NLP assistant whose purpose is to solve reading comprehension problems. You will be provided questions on a set of passages and you will need to provide the answer as it appears in the passage. The answer should be in the same language as the question and the passage.",
    "tydiqa": "You are an NLP assistant whose purpose is to solve reading comprehension problems. You will be provided questions on a set of passages and you will need to provide the answer as it appears in the passage. The answer should be in the same language as the question and the passage.",
    "panx": "You are an NLP assistant whose purpose is to perform Named Entity Recognition (NER). NER involves identifying and classifying named entities in a text into predefined categories such as person names, organizations, locations, and others. You will need to use the tags defined below:\nO means the word doesn’t correspond to any entity.\nB-PER/I-PER means the word corresponds to the beginning of/is inside a person entity.\nB-ORG/I-ORG means the word corresponds to the beginning of/is inside an organization entity.\nB-LOC/I-LOC means the word corresponds to the beginning of/is inside a location entity.\nDo not try to answer the question! Just tag each token in the sentence.",
    "gluecos_sentiment": "You are an NLP assistant whose purpose is to solve Sentiment Analysis problems. Sentiment Analysis is the task of determining whether the sentiment, opinion or emotion expressed in a textual data is: positive, negative, or neutral. Answer as concisely as possible in the same format as the examples below:",
    "xcopa": "You are an AI assistant whose purpose is to perform open-domain commonsense causal reasoning. You will be provided a premise and two alternatives, where the task is to select the alternative that more plausibly has a causal relation with the premise. Answer as concisely as possible in the same format as the examples below:",
    "paws-x": "You are an NLP assistant whose purpose is to perform Paraphrase Identification. The goal of Paraphrase Identification is to determine whether a pair of sentences have the same meaning. Answer as concisely as possible in the same format as the examples below:",
    "xlsum": "You are an NLP assistant whose purpose is to summarize any given article. You should summarize all important information concisely in the same language in which you have been provided the document. Following the examples provided below:",
    "sa": """Instruction:\nGiven a sentence, predict its sentiment as either """,
    "sib":"""Instruction:
Given a sentence, predict its topic from one of the following categories: """,
# ...
    "belebele": """Instruction:
Given a passage and a question, select the correct answer from the provided options. Read the passage carefully and choose the option that best answers the question based on the information given in the passage. Answer as concisely as possible in the same format as the examples below:
""",

"sdqa": """Instruction:
Given a context and a question, provide an answer to the question based on the information in the context.
The answer should be a span of text extracted directly from the context.
If the context does not contain enough information to answer the question, respond with "No answer".
Answer as concisely as possible in the same format as the examples below:
""",

"udp": """Instruction:
Given a sentence, its lemmas predict the dependency relation and head index for each token in the sentence.
A list of dependency relations is given below:
Deprel_list = = {deprel_list}

Input format:
Sentence: <space-separated tokens>
Lemmas: <space-separated lemmas>
Output format:
1    <token1>    <lemma1>    <predicted_deprel1>    <predicted_head1>
2    <token2>    <lemma2>    <predicted_deprel2>    <predicted_head2>
...
n    <tokenn>    <lemman>    <predicted_depreln>    <predicted_headn>
""",

"pos": """Instruction:
Given a sentence as space-separatd tokens, predict the Part of Speech (PoS) tags for each token. You will need to use the tags defined below:
TAGS: {upos_list}

Input format:
Sentence: <space-separated tokens>
Output format:
1    <token1>    <predicted_tag1>
2    <token2>    <predicted_tag2>
...
n    <tokenn>    <predicted_tagn>
""",

"ner": """Instruction:
Given a sentence as space-separatd tokens, predict the Named Entity Recogniton (NER) tags for each token. You will need to use the tags defined below:
TAGS: {ner_list}

Input format:
Sentence: <space-separated tokens>
Output format:
1    <token1>    <predicted_tag1>
2    <token2>    <predicted_tag2>
...
n    <tokenn>    <predicted_tagn>
""",
}

EXAMPLE_PROMPTS={

"sa": """Sentence: {input_sentence}
Sentiment: """,

"nli": """Premise: {premise}
Hypothesis: {hypothesis}
Relationship: """,

"sib": """Sentence: {sentence}
Topic: """,

"belebele_test": """Passage: {flores_passage}
Question: {question}
Options:
1. {mc_answer1}
2. {mc_answer2}
3. {mc_answer3}
4. {mc_answer4}
Answer: """,

"belebele_train": """Passage: {passage}
Question: {question}
Options:
1. {answer1}
2. {answer2}
3. {answer3}
4. {answer4}
Answer: """,

"sdqa": """Context: {context}
Question: {question}
Answer: """,

"udp": """Input:
Sentence: {sentence}
Lemmas: {lemmas}
Output:
""",

"pos": """Input:
Sentence: {sentence}
Output:
""",

"ner": """Input:
Sentence: {sentence}
Output:
"""
}

UD_HEAD_LABELS = [
    "_",
    "acl",
    "advcl",
    "advmod",
    "amod",
    "appos",
    "aux",
    "case",
    "cc",
    "ccomp",
    "clf",
    "compound",
    "conj",
    "cop",
    "csubj",
    "dep",
    "det",
    "discourse",
    "dislocated",
    "expl",
    "fixed",
    "flat",
    "goeswith",
    "iobj",
    "list",
    "mark",
    "nmod",
    "nsubj",
    "nummod",
    "obj",
    "obl",
    "orphan",
    "parataxis",
    "punct",
    "reparandum",
    "root",
    "vocative",
    "xcomp",
    'dup',
    'mwe',
    'name',
    'remnant'
]

UPOS_LABELS = ['NOUN', 'PUNCT', 'ADP', 'NUM', 'SYM', 'SCONJ', 'ADJ', 'PART', 'DET', 'CCONJ', 'PROPN', 'PRON', 'X', '_', 'ADV', 'INTJ', 'VERB', 'AUX', 'CONJ', 'root']
WIKIANN_LABELS = [
                            "O",
                            "B-PER",
                            "I-PER",
                            "B-ORG",
                            "I-ORG",
                            "B-LOC",
                            "I-LOC",
                        ]
NORWEGIAN_NER_LABELS = [
                                "O",
                                "B-OTH",
                                "I-OTH",
                                "E-OTH",
                                "S-OTH",
                                "B-ORG",
                                "I-ORG",
                                "E-ORG",
                                "S-ORG",
                                "B-PRS",
                                "I-PRS",
                                "E-PRS",
                                "S-PRS",
                                "B-GEO",
                                "I-GEO",
                                "E-GEO",
                                "S-GEO",
                            ]
NORWEGIAN_NER_LANGS= ['bokmaal', 'nynorsk', 'samnorsk']