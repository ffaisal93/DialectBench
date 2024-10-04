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

"did_instruction_arabic" : """
Instruction: Given a sentence, identify the Arabic city-level dialect. The options are: SAN, ALX, JED, RIY, ALG, BAG, DAM, BEN, BEI, RAB, AMM, JER, MUS, SFX, TUN, MOS, FES, CAI, DOH, TRI, KHA, ALE, BAS, MSA, ASW, SAL.

Example Sentences:

1. **SAN**:
   - Sentence: عفوا، لكن اشتي اسير للفندق حقي.
   - Sentence: شا اخرج حوالي الساعه تسع.
   - Sentence: لو كنت استسلمت احسن.
   **Explanation**: "اشتي" and "اشل" are unique to Yemeni.

2. **ALX**:
   - Sentence: القطر هيوصل الساعم كام؟
   - Sentence: أنا استمتعت بإقامتى.
   - Sentence: ممكن تبدل الكراسى معايا؟
   **Explanation**: "هيوصل" and "معايا" are Alexandrian.

3. **JED**:
   - Sentence: ابا دونات، لو سمحت.
   - Sentence: وريني ساعات رجالية لو سمحت.
   - Sentence: أبا شيء جديد.
   **Explanation**: "أبا" (I want) is specific to Jeddah.

4. **RIY**:
   - Sentence: طيب سيدي. وش تبغى للحلى؟
   - Sentence: انت فاضي السبت الجاي؟
   - Sentence: شفت أسعار بهالرخص؟
   **Explanation**: "وش" and "تبغى" are Najdi expressions.

5. **ALG**:
   - Sentence: كي نشوف الأسعار ناقصة.
   - Sentence: راه ماشي ديركت لهناك.
   - Sentence: تبانلي سخافة نشري أي حاجة.
   **Explanation**: "راه" and "كي" are typical in Algerian Arabic.

6. **BAG**:
   - Sentence: ممكن نشوف محافظ جلدية؟
   - Sentence: ما تشتغل، مو؟
   - Sentence: تكدر تنتقل للمعقد الشاغر؟
   **Explanation**: "تكدر" and "مو" are markers of Baghdadi.

7. **DAM**:
   - Sentence: الطرف التاني عالخط.
   - Sentence: ما فيك تفوت ألعاب نارية.
   - Sentence: هاد آخر شي؟
   **Explanation**: "عالخط" and "هاد" are Damascene.

8. **BEN**:
   - Sentence: نقدر نستعمل تليفونك؟
   - Sentence: ممكن تعطيني علم قبل ما نوصل؟
   - Sentence: أنا من اسبانيا.
   **Explanation**: "تعطيني علم" is common in Benghazi.

9. **BEI**:
   - Sentence: أياهن أهم بالنسبة إلكن؟
   - Sentence: رفيئي زحط.
   - Sentence: رح يكون في شوي تاخير.
   **Explanation**: "رفيئي" and "إلكن" are used in Beirut.

10. **RAB**:
    - Sentence: فاياش مختصين؟
    - Sentence: إينا نوع دالعصير بغيتي؟
    - Sentence: مرحبا. كي داير؟
    **Explanation**: "بغيتي" and "كي داير" are Moroccan expressions.

11. **AMM**:
    - Sentence: بدي كريم ليلي.
    - Sentence: بدي كرسي مريح.
    - Sentence: في بنك بالمنطقة؟
    **Explanation**: "بدي" is unique to Amman’s dialect.

12. **JER**:
    - Sentence: بتحب أخليه يرجع يحكي؟
    - Sentence: رح أضل لبكرا.
    - Sentence: بكون مبسوط.
    **Explanation**: "بكون" and "مبسوط" are specific to Jerusalem.

13. **MUS**:
    - Sentence: عرفت شو هو الغلط.
    - Sentence: هل يميل الكثير إلى نسيان؟
    - Sentence: انزين، خلنا نذهب.
    **Explanation**: "خلنا" and "انزين" are used in Muscat.

14. **SFX**:
    - Sentence: انجم نمشي بالميترو؟
    - Sentence: العفو.
    - Sentence: نحتوا حوايجنا.
    **Explanation**: "انجم" and "حوايج" are typical in Sfax.

15. **TUN**:
    - Sentence: البوابة اسابعة.
    - Sentence: باش نخرج.
    - Sentence: تنجم تبعث حمال؟
    **Explanation**: "باش" and "تنجم" are Tunisian.

16. **MOS**:
    - Sentence: هو سباطعش ايه؟
    - Sentence: اوه، انا اسف.
    - Sentence: اخاف اكو خطأ.
    **Explanation**: "اخاف" is distinct to Mosul.

17. **FES**:
    - Sentence: غي شوية ديال الناس.
    - Sentence: راه كاين فنواحي.
    - Sentence: عطيني جوج تذكيرات.
    **Explanation**: "غي" and "راه" are from Fes dialect.

18. **CAI**:
    - Sentence: بنسافر تلات مرات.
    - Sentence: ممكن تضيقلي الفستان؟
    - Sentence: عشر دولارات للتاكسي؟
    **Explanation**: "تلات" and "حيكفي" are used in Cairo.

19. **DOH**:
    - Sentence: ورني واحد حق حرمة.
    - Sentence: بترجع بيتكم؟
    - Sentence: بغيتك تنظف.
    **Explanation**: "حق" and "بغيتك" are from Doha.

20. **TRI**:
    - Sentence: مكان واعر تلقاه.
    - Sentence: قعمز و استنى.
    - Sentence: نرجعلك توا.
    **Explanation**: "قعمز" and "توا" are unique to Tripoli.

21. **KHA**:
    - Sentence: ح أحضر المدرسة.
    - Sentence: ممكن احصل على رقم؟
    - Sentence: دايرين طربيزة جنب المنصة.
    **Explanation**: "ح" and "طربيزة" are specific to Khartoum.

22. **ALE**:
    - Sentence: ممكن أقترح وحدة؟
    - Sentence: وين موقف الباص؟
    - Sentence: ما منظرك أكبر.
    **Explanation**: "تبع" and "في عنا" are Aleppine.

23. **BAS**:
    - Sentence: هاي الاحذية قوية؟
    - Sentence: اريد ارتاح.
    - Sentence: اكو حد يساعدني.
    **Explanation**: "اكو" and "اريد" are from Basra.

24. **MSA**:
    - Sentence: هل هناك صناديق بريد؟
    - Sentence: هل تمانع اذا؟
    - Sentence: تشغل أشخاصاً جدد.
    **Explanation**: Standard Arabic.

25. **ASW**:
    - Sentence: خدني لطريق.
    - Sentence: متلمسنيش.
    - Sentence: هاخد سبرايت.
    **Explanation**: "هاخد" and "متلمسنيش" are Aswani.

26. **SAL**:
    - Sentence: أي واحد بتفضل؟
    - Sentence: رقم غرفتي.
    - Sentence: من الصبح.
    **Explanation**: "بتقدر" and "غسيلي" are from Salalah.

Sentence: {input_sentence}  
Dialect:
"""

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