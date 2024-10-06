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
    "did":"""Instruction:
Given a sentence, predict in which dialect it is written. The options are: """,
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
Given a sentence, its lemmas (if available, otherwise '_') predict the dependency relation and head index for each token in the sentence.
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

"did_instruction_arabic_1" : """
Instruction: Given a sentence, identify the Arabic city-level dialect.

Examples:
SAN: عفواً، اشتي اسير للفندق حقي. ("اشتي" is unique to Yemeni).
ALX: القطر هيوصل الساعة كام؟ ("هيوصل" is Alexandrian).
JED: ابا دونات، لو سمحت. ("ابا" is specific to Jeddah).
RIY: وش تبغى للحلى؟ ("وش" is Najdi).
ALG: كي نشوف الأسعار ناقصة. ("كي" is Algerian).
BAG: تكدر تنتقل للمعقد الشاغر؟ ("تكدر" is Baghdadi).
DAM: الطرف التاني عالخط. ("عالخط" is Damascene).
BEN: ممكن تعطيني علم قبل ما نوصل؟ ("تعطيني علم" is Benghazi).
BEI: رفيئي زحط. ("رفيئي" is from Beirut).
RAB: كي داير؟ ("كي داير" is Moroccan).
AMM: بدي كريم ليلي. ("بدي" is Ammani).
JER: بكون مبسوط. ("بكون" is from Jerusalem).
MUS: انزين، خلنا نذهب. ("انزين" is Muscati).
SFX: انجم نمشي بالميترو؟ ("انجم" is Sfaxian).
TUN: باش نخرج. ("باش" is Tunisian).
MOS: اخاف اكو خطأ. ("اخاف" is Mosuli).
FES: راه كاين فنواحي. ("راه" is from Fes).
CAI: ممكن تضيقلي الفستان؟ ("تضيقلي" is Cairene).
DOH: بغيتك تنظف. ("بغيتك" is Qatari).
TRI: قعمز و استنى. ("قعمز" is Tripolitan).
KHA: ح أحضر المدرسة. ("ح" is Khartoumi).
ALE: وين موقف الباص؟ ("وين" is Aleppine).
BAS: اكو حد يساعدني. ("اكو" is Basrawi).
MSA: هل هناك صناديق بريد؟ (Standard Arabic).
ASW: هاخد سبرايت. ("هاخد" is Aswani).
SAL: بتقدر تعطيني؟ ("بتقدر" is from Salalah).

Options: SAN, ALX, JED, RIY, ALG, BAG, DAM, BEN, BEI, RAB, AMM, JER, MUS, SFX, TUN, MOS, FES, CAI, DOH, TRI, KHA, ALE, BAS, MSA, ASW, SAL.

Now predict the dialect:

Sentence: هاي الاحذية قوية؟  
Dialect: BAS

Sentence: ممكن أقترح وحدة؟
Dialect: ALE

Sentence: هل هناك صناديق بريد؟
Dialect: MSA

Sentence: {input_sentence}  
Dialect: """,

## learning from 3 example
"did_instruction_arabic_2": """
Given a sentence, identify the Arabic city-level dialect. Each dialect has unique linguistic features such as vocabulary, phonetic variations, or sentence structure that distinguish it from others. Consider the following descriptions and examples to guide your selection:

Examples:

SAN: Yemeni Arabic spoken in Sana'a is characterized by unique verbs like "اشتي" for "I want."
ALX: Alexandrian Arabic uses distinct phrases like "هيوصل" for "arrive."
JED: Jeddah's dialect features expressions like "ابا" for "I want," differing from other Saudi dialects.
RIY: Najdi Arabic, spoken in Riyadh, uses "وش" and "تبغى," which are absent in western Saudi varieties.
ALG: Algerian Arabic employs markers like "راه" and "كي," often shared across North African dialects.
BAG: Baghdadi Arabic uses unique terms such as "تكدر" and "مو" for "can" and "not," respectively.
DAM: Damascene Arabic has phrases like "عالخط" and "هاد" that are uncommon outside Syria.
BEN: The Benghazi dialect includes expressions like "تعطيني علم," reflecting its Libyan roots.
BEI: Beirut’s Lebanese Arabic features phrases like "رفيئي" for "friend."
RAB: Moroccan Arabic, spoken in Rabat, uses "بغيتي" and "كي داير" for "want" and "how are you?"
AMM: Ammani Jordanian Arabic often starts sentences with "بدي" meaning "I want."
JER: Jerusalem's dialect includes "بكون" and "مبسوط" for "I am" and "happy."
MUS: Muscati Arabic is marked by "انزين" and "خلنا," showing Gulf influences.
SFX: The Sfaxian dialect in Tunisia uses terms like "انجم" for "can I," distinct from other Tunisian varieties.
TUN: Tunisian Arabic frequently features "باش" for future tense, unlike its Algerian counterpart.
MOS: Mosuli Iraqi Arabic uses "اخاف" for "I am afraid," differentiating it from Baghdadi.
FES: The Fes dialect includes "غي" and "راه," shared with other Moroccan varieties.
CAI: Cairene Arabic has unique terms like "تضيقلي" for "make tighter."
DOH: Doha’s Qatari dialect uses "بغيتك" for "I want you to."
TRI: Tripolitanian Libyan Arabic is distinct with expressions like "قعمز" for "sit."
KHA: Khartoumi Sudanese Arabic uses "ح" for future tense and "طربيزة" for "table."
ALE: Aleppine Syrian Arabic includes "وين" for "where."
BAS: Basrawi Iraqi Arabic is marked by "اكو" for "there is."
MSA: Modern Standard Arabic (MSA) is the formal version of Arabic used in media and literature.
ASW: Aswani Egyptian Arabic features "هاخد" for "I will take," reflecting Upper Egyptian speech.
SAL: Salalah's Omani Arabic includes "بتقدر" for "can you," showcasing southern Omani influence.
Options: SAN, ALX, JED, RIY, ALG, BAG, DAM, BEN, BEI, RAB, AMM, JER, MUS, SFX, TUN, MOS, FES, CAI, DOH, TRI, KHA, ALE, BAS, MSA, ASW, SAL.

Question: Given the unique features of each dialect, identify which one matches the sentence below.

Sentence: هاي الاحذية قوية؟  
Dialect: BAS

Sentence: ممكن أقترح وحدة؟
Dialect: ALE

Sentence: هل هناك صناديق بريد؟
Dialect: MSA

Sentence: {input_sentence}  
Dialect: """,

## learning from 10 example
"did_instruction_arabic_10": """
Instruction: Given a sentence, identify the Arabic city-level dialect based on distinctive vocabulary and sentence structure cues. Below are some characteristics for each dialect:

- KHA: Uses terms like "ح" for future tense, "زول" for person, and phrases such as "ممكن ترسل حمال؟" for service requests.
- RAB: Moroccan Arabic with expressions like "عافاك" (please), "بغيت" (want), and "كاين" (there is).
- ALG: Algerian Arabic features "واش" (what), "راني" (I am), and heavy use of French-influenced phrases.
- JED: Hejazi Arabic marked by "أبا" (I want), "فين" (where), and common use of polite forms.
- CAI: Egyptian Arabic with "عايز" (want), "مش" (not), and distinct negation patterns.
- MOS: Iraqi Arabic, using "غاح" for future and "ماشي" for okay. Soft consonant pronunciations.
- ALE: Northern Syrian Arabic using "شقد" (how much) and "بدي" (I want).
- SFX: Tunisian Arabic with "تنجم" (can) and "نحب" (want), showing unique local vocabulary.
- BEN: Libyan Arabic marked by "توا" (now), "نبي" (want), and "شن" (what).
- BAG: Central Iraqi Arabic using "اكو" (there is), "شلون" (how), and phrases like "ماكو" (none).
- RIY: Najdi dialect featuring "وش" (what), "تبغى" (want), and a Bedouin-influenced style.
- BEI: Lebanese Arabic with "عم" for progressive, "إزا" (if), and mixed French/English terms.
- MSA: Modern Standard Arabic, formal and lacking colloquial elements. Used in official contexts.
- ASW: Upper Egyptian Arabic with unique elongated vowels and specific expressions like "همشي" (I will go).
- TRI: Libyan dialect using "قداش" (how much), "نبي" (want), and distinct local vocabulary.
- FES: Moroccan dialect with phrases like "فين" (where) and "راه" (is), specific to the Fes region.
- BAS: Southern Iraqi Arabic using "اكو" (there is), "شلون" (how), and softer pronunciation.
- MUS: Omani Arabic with "أبغا" (want) and "وايد" (a lot), more formal in tone.
- TUN: Tunisian Arabic with "باش" (will) and "نحب" (want), with a mix of French and local words.
- JER: Palestinian Arabic using "بدي" (want), "كتير" (a lot), with strong Levantine influence.
- SAL: Southern Omani Arabic using "قديش" (how much) and "بتقدر" (can you).
- AMM: Jordanian Arabic featuring "بدي" (want) and "شو" (what), distinct from Palestinian intonation.
- ALX: Egyptian Arabic from Alexandria, using "أيوة" (yes), "عايز" (want), with local flavor.
- DAM: Syrian Arabic marked by "كتير" (a lot), "بدك" (you want), and softened consonants.
- DOH: Qatari Arabic with "بغيت" (want) and "يصير" (can), typical of Gulf Arabic.
- SAN: Yemeni Arabic using "اشتي" (I want) and phrases like "عيقدر" (can), with unique phonetics.

Options: SAN, ALX, JED, RIY, ALG, BAG, DAM, BEN, BEI, RAB, AMM, JER, MUS, SFX, TUN, MOS, FES, CAI, DOH, TRI, KHA, ALE, BAS, MSA, ASW, SAL.

Question: Given the unique features of each dialect, identify which one matches the sentence below.

Sentence: هاي الاحذية قوية؟  
Dialect: BAS

Sentence: ممكن أقترح وحدة؟
Dialect: ALE

Sentence: هل هناك صناديق بريد؟
Dialect: MSA

Sentence: {input_sentence}  
Dialect: """,

## learning from 30 example
"did_instruction_arabic_30": """
Instruction: Given a sentence, identify the Arabic city-level dialect based on distinctive vocabulary, grammar, phonetic features, and cultural context. Consider the following:

- Vocabulary Specificity: Observe unique word choices and their variations, like "بغيت" (RAB) vs. "داير" (KHA) for "want."
- Grammar and Sentence Structure: Pay attention to omitted or included auxiliary verbs, connectors, and sentence patterns.
- Expressions and Idioms: Identify regional expressions and idioms, e.g., "شنو" (FES) vs. "شن" (BEN).
- Politeness and Request Forms: Look for politeness markers and how they are positioned in a sentence, like "عافاك" (RAB) or "من فضلك" (CAI).
- Loanwords and Language Influence: Recognize loanwords and mixed lexicons, such as French in ALG, SFX, and RAB.
- Formal vs. Informal Register: Note whether the sentence sounds formal or casual based on its word choice and structure.
- Pronunciation Markers: Identify dialect-specific pronunciation cues like "چ" (BAG), "گ" (MOS), or "ت" instead of "ث" (CAI).
- Unique Contextual Markers: Consider common topics and context-specific phrases relevant to certain regions, like references to food, transport, or family.

Here are some dialect markers for each region:

- KHA (Khartoum): Sudanese Arabic with "داير" (want), "عفواً" (excuse me), and a focus on polite, formal expressions.
- RAB (Rabat): Moroccan Arabic featuring "عافاك" (please), "واخا" (okay), and phrases with "بغيت" (want).
- ALG (Algiers): Algerian Arabic using "واش" (what), "راني" (I am), and frequent French loanwords.
- JED (Jeddah): Hejazi Arabic with "أبغا" (want), "فين" (where), and soft Bedouin intonations.
- CAI (Cairo): Egyptian Arabic marked by "عايز" (want), "إيه" (what), and informal, humorous tone.
- MOS (Mosul): Iraqi Arabic with "غاح" (will), "اتطيق" (can), and local pronunciation nuances like "چ" and "گ".
- ALE (Aleppo): Northern Syrian Arabic using "بدي" (I want), "قديش" (how much), and frequent Turkish borrowings.
- SFX (Sfax): Tunisian Arabic with "باش" (will), "نحب" (want), and French influences in daily speech.
- BEN (Benghazi): Libyan Arabic with "توا" (now), "نبي" (want), and expressions like "شن" (what).
- BAG (Baghdad): Central Iraqi Arabic marked by "شلون" (how), "اكو" (there is), and "ماكو" (none).
- RIY (Riyadh): Najdi dialect using "وش" (what), "تبغى" (want), and strong, formal tones.
- BEI (Beirut): Lebanese Arabic with "عم" (progressive), "إزا" (if), and a mix of French/English terms.
- MSA (Modern Standard Arabic): Formal Arabic used in official contexts, news, and academic discourse.
- ASW (Aswan): Upper Egyptian Arabic with distinct phrases like "همشي" (I will go) and local modifications.
- TRI (Tripoli): Libyan dialect with "قداش" (how much), "نبي" (want), and unique phrasing.
- FES (Fes): Moroccan dialect with "فين" (where), "راه" (is), and distinctive sentence endings.
- BAS (Basra): Southern Iraqi Arabic with softer pronunciation and "اكو" (there is).
- MUS (Muscat): Omani Arabic featuring "أبغا" (want), "وايد" (a lot), and formal-sounding requests.
- TUN (Tunis): Tunisian Arabic marked by "باش" (will), "نحب" (want), and local French vocabulary.
- JER (Jerusalem): Palestinian Arabic with "بدي" (want), "كتير" (a lot), and a melodious intonation.
- SAL (Salalah): Southern Omani Arabic using "قديش" (how much), "بتقدر" (can you), and distinctive phrasing.
- AMM (Amman): Jordanian Arabic with "بدي" (want), "شو" (what), and more formal Levantine tone.
- ALX (Alexandria): Egyptian Arabic with "أيوة" (yes), "عايز" (want), and Alexandrian pronunciation.
- DAM (Damascus): Syrian Arabic with "كتير" (a lot), "بدك" (you want), and softer, extended vowels.
- DOH (Doha): Qatari Arabic using "بغيت" (want), "يصير" (can), and Gulf-influenced speech.
- SAN (Sanaa): Yemeni Arabic with "اشتي" (I want) and unique contextual references.


Options: SAN, ALX, JED, RIY, ALG, BAG, DAM, BEN, BEI, RAB, AMM, JER, MUS, SFX, TUN, MOS, FES, CAI, DOH, TRI, KHA, ALE, BAS, MSA, ASW, SAL.

Question: Given the unique features of each dialect, identify which one matches the sentence below.

Sentence: هاي الاحذية قوية؟  
Dialect: BAS

Sentence: ممكن أقترح وحدة؟
Dialect: ALE

Sentence: هل هناك صناديق بريد؟
Dialect: MSA

Sentence: {input_sentence}  
Dialect: """,

## learning from 50 example
"did_instruction_arabic_50": """
Instruction: Given a sentence, identify the Arabic city-level dialect based on refined distinctions in vocabulary, grammar, pronunciation, formality, and cultural context. Consider the following:

1. Vocabulary & Word Usage:
   - Identify regional preferences in word choice and semantics.
   - Distinguish phrases with nuanced differences like "بغيت" (RAB, TRI) vs. "عايز" (CAI) or "داير" (KHA).
   
2. Grammar & Sentence Structure:
   - Consider omitted or added auxiliaries, distinct use of sentence connectors, and grammatical patterns.

3. Cultural Markers & Idioms:
   - Look for culturally specific idioms, proverbs, or regional markers indicating local customs.
   - Examples: DAM tends to use phrases emphasizing family, while FES focuses on politeness in negotiation.

4. Pronunciation Cues:
   - Pay close attention to phonetic variations like "چ" (BAG), "گ" (MOS), or "ت" for "ث" (CAI).
   - Note any systematic consonant or vowel shifts reflecting regional accents.

5. Formality and Context:
   - Observe shifts in tone, politeness markers, or directness based on context (formal, casual, professional).

6. Loanwords & External Influence:
   - Note heavy use of French (ALG, SFX) or English (RIY, DOH) borrowings.
   - Examples: "سي دي" (CD), "كازينو" (casino), "فوتر" (voucher).

7. Expressions Indicating Social Hierarchy:
   - Politeness, honorifics, or phrases indicating social standing are more frequent in certain dialects like RAB and BEI.

### Dialect-Specific Markers:
- KHA (Khartoum): Sudanese Arabic featuring "داير" (want), local terms like "متين" (when), and polite formal requests.
- RAB (Rabat): Moroccan Arabic using "عافاك" (please), "بغيت" (want), and intricate negotiation-related terms.
- ALG (Algiers): Algerian Arabic marked by "واش" (what), French terms like "شحال" (how much), and mixed linguistic patterns.
- JED (Jeddah): Hejazi Arabic with "أبغا" (want), "فين" (where), and hospitality-driven expressions.
- CAI (Cairo): Egyptian Arabic with "عايز" (want), "فين" (where), and humor-tinged colloquialisms.
- MOS (Mosul): Iraqi Arabic with "چ" (ch sound), "گ" (g sound), and local vocabulary.
- ALE (Aleppo): Northern Syrian Arabic with "بدي" (I want), "قديش" (how much), and Turkish loanwords.
- SFX (Sfax): Tunisian Arabic featuring "باش" (will), "نحب" (want), and French-infused expressions.
- BEN (Benghazi): Libyan Arabic with "شن" (what), "توا" (now), and "نبي" (want).
- BAG (Baghdad): Central Iraqi Arabic marked by "شلون" (how), "ماكو" (none), and pronounced local pronunciation.
- RIY (Riyadh): Najdi dialect using "وش" (what), "تبغى" (want), and direct, formal phrasing.
- BEI (Beirut): Lebanese Arabic with "عم" (progressive), "إزا" (if), and blended French and English terms.
- MSA (Modern Standard Arabic): Formal Arabic used in media, academic, and professional settings.
- ASW (Aswan): Upper Egyptian Arabic with distinct local expressions and tonal shifts.
- TRI (Tripoli): Libyan Arabic with "قداش" (how much), "نبي" (want), and negotiation-focused terms.
- FES (Fes): Moroccan Arabic marked by negotiation and politeness nuances.
- BAS (Basra): Southern Iraqi Arabic with a softer pronunciation, using "اكو" and "ماكو".
- MUS (Muscat): Omani Arabic featuring formal and polite phrases like "أبغا" (want) and "يصير" (can).
- TUN (Tunis): Tunisian Arabic with French influences and context-sensitive terms.
- JER (Jerusalem): Palestinian Arabic using "بدي" (want), melodic intonations, and social context markers.
- SAL (Salalah): Southern Omani Arabic using "قديش" (how much), and distinctive phrasing.
- AMM (Amman): Jordanian Arabic with more formal Levantine tones.
- ALX (Alexandria): Egyptian Arabic with humor-infused phrases and local twists.
- DAM (Damascus): Syrian Arabic using "بدك" (you want), formal phrasing, and softer intonations.
- DOH (Doha): Qatari Arabic using "بغيت" (want), and Gulf-inflected vocabulary.
- SAN (Sanaa): Yemeni Arabic with unique local references and vocabulary.

Options: SAN, ALX, JED, RIY, ALG, BAG, DAM, BEN, BEI, RAB, AMM, JER, MUS, SFX, TUN, MOS, FES, CAI, DOH, TRI, KHA, ALE, BAS, MSA, ASW, SAL.

Question: Given the unique features of each dialect, identify which one matches the sentence below.

Sentence: هاي الاحذية قوية؟  
Dialect: BAS

Sentence: ممكن أقترح وحدة؟
Dialect: ALE

Sentence: هل هناك صناديق بريد؟
Dialect: MSA

Sentence: {input_sentence}  
Dialect: """,

}

EXAMPLE_PROMPTS={

"sa": """Sentence: {input_sentence}
Sentiment: """,

"did": """Sentence: {input_sentence}
Dialect: """,

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
