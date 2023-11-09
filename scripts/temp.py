import json
from itertools import chain
from datasets import load_dataset,DatasetDict
from transformers import (
    CONFIG_MAPPING,
    MODEL_MAPPING,
    AutoConfig,
    AutoModelForMultipleChoice,
    AutoTokenizer,
    PreTrainedTokenizerBase,
    SchedulerType,
    default_data_collator,
    get_scheduler,
)


sdqa_ex = {
	"context": ["Architecturally, the school has a Catholic character. Atop the Main Building's gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.Architecturally, the school has a Catholic character. Atop the Main Building's gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.Architecturally, the school has a Catholic character. Atop the Main Building's gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary."],
	"question": ["To whom did the Virgin Mary allegedly appear in 1858 in Lourdes France?"],
	"answer":[{"text": [ "Saint Bernadette Soubirous" ], "answer_start": [ 515 ]}]
} 


mc_ex = {"link":"https:\/\/en.wikibooks.org\/wiki\/Accordion\/Right_hand","question_number":1,"flores_passage":"Make sure your hand is as relaxed as possible while still hitting all the notes correctly - also try not to make much extraneous motion with your fingers. This way, you will tire yourself out as little as possible. Remember there's no need to hit the keys with a lot of force for extra volume like on the piano. On the accordion, to get extra volume, you use the bellows with more pressure or speed.","question":"According to the passage, what would not be considered an accurate tip for successfully playing the accordion?","mc_answer1":"For additional volume, increase the force with which you hit the keys","mc_answer2":"Keep unnecessary movement to a minimum in order to preserve your stamina","mc_answer3":"Be mindful of hitting the notes while maintaining a relaxed hand","mc_answer4":"Increase the speed with which you operate the bellows to achieve extra volume","correct_answer_num":"1","dialect":"eng_Latn","ds":"2023-05-03"}

def prepare_train_qa_features(examples):
	# Some of the questions have lots of whitespace on the left, which is not useful and will make the
	# truncation of the context fail (the tokenized question will take a lots of space). So we remove that
	# left whitespace
	question_column_name="question"
	context_column_name="context"
	answer_column_name="answer"
	pad_on_right=True
	doc_stride=5
	max_seq_length=512
	pad_to_max_length=True
	examples[question_column_name] = [q.lstrip() for q in examples[question_column_name]]
	# Tokenize our examples with truncation and maybe padding, but keep the overflows using a stride. This results
	# in one example possible giving several features when a context is long, each of those features having a
	# context that overlaps a bit the context of the previous feature.
	tokenized_examples = tokenizer(
	    examples[question_column_name if pad_on_right else context_column_name],
	    examples[context_column_name if pad_on_right else question_column_name],
	    truncation="only_second" if pad_on_right else "only_first",
	    max_length=max_seq_length,
	    stride=doc_stride,
	    return_overflowing_tokens=True,
	    return_offsets_mapping=True,
	    padding="max_length" if pad_to_max_length else False,
	)
	print(tokenized_examples.tokens())

def preprocess_function(examples):
    print(examples)
    first_sentences = [[context[:10]] * 4 for context in examples[context_name]]
    question_headers = examples[question_header_name]
    second_sentences = [
        [f"{header} {examples[end][i][:10]}" for end in ending_names] for i, header in enumerate(question_headers)
    ]
    print(first_sentences)
    print(second_sentences)

    # Flatten out
    first_sentences = list(chain(*first_sentences))
    second_sentences = list(chain(*second_sentences))
    
    print(first_sentences)
    print(second_sentences)

    # Tokenize
    tokenized_examples = tokenizer(
        first_sentences,
        second_sentences,
        truncation=True,
        max_length=max_seq_length,
        padding="max_length" if pad_to_max_length else False,
        stride=4
    )
    print(tokenized_examples)
    # Un-flatten
    return {k: [v[i : i + 4] for i in range(0, len(v), 4)] for k, v in tokenized_examples.items()}




if __name__ == '__main__':
	tokenizer = AutoTokenizer.from_pretrained(
            'bert-base-multilingual-cased')

	prepare_train_qa_features(sdqa_ex)