from instructions import INSTRUCTIONS, EXAMPLE_PROMPTS, UD_HEAD_LABELS, UPOS_LABELS, WIKIANN_LABELS
import random

class PreambleCreator:
    @staticmethod
    def create_preamble_sa(dataset):
        labels = set(dataset['label'])
        prompt = INSTRUCTIONS['sa']
        for i, label in enumerate(labels):
            if i < len(labels) - 1:
                prompt += f"{label}, "
            else:
                prompt += f"or {label}.\n"
        preamble = prompt
        return preamble

    @staticmethod
    def create_preamble_sib(dataset):
        labels = set(dataset['label'])
        prompt = INSTRUCTIONS['sib']
        for i, label in enumerate(labels):
            if i < len(labels) - 1:
                prompt += f"{label}, "
            else:
                prompt += f"{label}.\n"
        preamble = prompt
        return preamble

    @staticmethod
    def create_preamble_did(dataset):
        labels = set(dataset['label'])
        prompt = INSTRUCTIONS['did']
        for i, label in enumerate(labels):
            if i < len(labels) - 1:
                prompt += f"{label}, "
            else:
                prompt += f"{label}.\n"
        preamble = prompt
        return preamble

    @staticmethod
    def create_preamble_belebele(dataset):
        preamble = INSTRUCTIONS['belebele']
        return preamble

    @staticmethod
    def create_preamble_nli(dataset):
        preamble = INSTRUCTIONS['nli']
        return preamble

    @staticmethod
    def create_preamble_sdqa():
        preamble = INSTRUCTIONS['sdqa']
        return preamble

    @staticmethod
    def create_preamble_udp():
        deprel_list = "{" + ", ".join(UD_HEAD_LABELS) + "}"
        preamble = INSTRUCTIONS['udp'].format(**{'deprel_list': deprel_list})
        return preamble

    @staticmethod
    def create_preamble_pos():
        upos_list = "{" + ", ".join(UPOS_LABELS) + "}"
        preamble = INSTRUCTIONS['pos'].format(**{'upos_list': upos_list})
        return preamble

    @staticmethod
    def create_preamble_ner():
        ner_list = "{" + ", ".join(WIKIANN_LABELS) + "}"
        preamble = INSTRUCTIONS['ner'].format(**{'ner_list': ner_list})
        return preamble


class PromptAdder:
    @staticmethod
    def add_prompted_udp(example):
        text = example['text']
        tokens = example['tokens']
        lemmas = example['lemmas']
        heads = example['head']
        deprels = example['deprel']
        
        sentence = ' '.join(tokens)
        joint_lemmas = ' '.join(lemmas)
        prompted_text = (EXAMPLE_PROMPTS['udp'].format(**{ 'sentence':sentence, 'lemmas':joint_lemmas}))
        
        # Construct the expected output
        output_lines = []
        for i, (token, lemma, head, deprel) in enumerate(zip(tokens, lemmas, heads, deprels), start=1):
            output_lines.append(f"{i} {token} {lemma} {deprel} {head}")
        expected_output = "\n".join(output_lines)
        
        # Add the prompt and expected output to the example
        prompted_example={}
        prompted_example['text'] = prompted_text
        prompted_example['deprel'] = deprels
        prompted_example['head'] = heads
        prompted_example['label_text'] = expected_output
        
        return prompted_example

    @staticmethod
    def add_prompted_pos(example):
        tokens = example['tokens']
        tags = example['upos']
        sentence = ' '.join(tokens)
        tag_labels= [UPOS_LABELS[x] for x in tags]
        prompted_text = (EXAMPLE_PROMPTS['pos'].format(**{ 'sentence':sentence}))

        # Construct the expected output
        output_lines = []
        for i, (token, tag) in enumerate(zip(tokens, tag_labels), start=1):
            output_lines.append(f"{i} {token} {tag}")
        expected_output = "\n".join(output_lines)
        
        # Add the prompt and expected output to the example
        prompted_example={}
        prompted_example['text'] = prompted_text
        prompted_example['label_text'] = expected_output
        
        return prompted_example

    @staticmethod
    def add_prompted_ner(example):
        tokens = example['tokens']
        tags = example['ner_tags']
        sentence = ' '.join(tokens)
        tag_labels= [WIKIANN_LABELS[x] for x in tags]
        prompted_text = (EXAMPLE_PROMPTS['ner'].format(**{ 'sentence':sentence}))

        # Construct the expected output
        output_lines = []
        for i, (token, tag) in enumerate(zip(tokens, tag_labels), start=1):
            output_lines.append(f"{i} {token} {tag}")
        expected_output = "\n".join(output_lines)
        
        # Add the prompt and expected output to the example
        prompted_example={}
        prompted_example['text'] = prompted_text
        prompted_example['label_text'] = expected_output
        
        return prompted_example

    @staticmethod
    def add_prompted_sa(example, dataset):
        prompted_text = (EXAMPLE_PROMPTS['sa'].format(**{'input_sentence': example['sentence']}))
        return {"text": prompted_text}

    @staticmethod
    def add_prompted_did(example, dataset):
        prompted_text = (EXAMPLE_PROMPTS['did'].format(**{'input_sentence': example['sentence']}))
        return {"text": prompted_text}

    @staticmethod
    def add_prompted_did_ablation_ara_1(example, dataset):
        prompted_text = (INSTRUCTIONS['did_instruction_arabic'].format(**{'input_sentence': example['sentence']}))
        return {"text": prompted_text}

    @staticmethod
    def add_prompted_nli(example, dataset):
        labels_dict = {0: 'entailment', 1: 'neutral', 2: 'contradiction'}
        prompted_text = (EXAMPLE_PROMPTS['nli'].format(**{'premise': example['premise'],
                                                           'hypothesis': example['hypothesis']}))
        return {"text": prompted_text, 'label_text': labels_dict[example['label']]}

    @staticmethod
    def add_prompted_sib(example, dataset):
        prompted_text = (EXAMPLE_PROMPTS['sib'].format(**{'sentence': example['sentence']}))
        return {"text": prompted_text}

    @staticmethod
    def add_prompted_belebele(example, dataset):
        prompted_text = (EXAMPLE_PROMPTS[f'belebele_{dataset}'].format(**example))
        return {"text": prompted_text}

    @staticmethod
    def add_prompted_sdqa(examples):
        for example in examples['paragraphs']:
            context = example['context']
            for qa in example['qas']:
                question = qa['question']
                answers = [ans['text'] for ans in qa['answers']]
                prompted_text = (EXAMPLE_PROMPTS['sdqa'].format(**{'context': context, 'question': question}))
        return {"text": prompted_text, 'label_text': answers}


class KShotExamplePreparer:
    @staticmethod
    def prepare_kshot(preamble, train_dataset, test_dataset, label_column, k, types='classification', prompt_type='gpt-35'):
        if k > 0:
            if types == 'classification':
                label_examples = {}
                for example in train_dataset:
                    label = example[label_column]
                    if label not in label_examples:
                        label_examples[label] = []
                    label_examples[label].append(example)
                k = max(k, sum(1 for examples in label_examples.values()))
                print(k)

                kshot_examples = []
                for label, examples in label_examples.items():
                    if k == 0:
                        break
                    kshot_examples.append(random.choice(examples))
                    k -= 1

                remaining_examples = [example for examples in label_examples.values() for example in examples if
                                      example not in kshot_examples]

                if k > -1:
                    kshot_examples.extend(random.sample(remaining_examples, k))
            elif types == 'generative':
                kshot_examples = random.sample(list(train_dataset), k)
            else:
                raise ValueError(f"Invalid type: {types}. Expected 'classification' or 'generative'.")

            prompt = preamble + "\n"

            for example in kshot_examples:
                text = example["text"]
                label = example[label_column]
                if isinstance(label, list):
                    label = label[0]
                prompt += f"{text}{label}\n\n"
        else:
            prompt = preamble + "\n"

        kshot_prompt = prompt
        prompted_test_examples = []
        for example in test_dataset:
            text = example["text"]
            prompt = kshot_prompt + f"{text} "
            prompted_test_examples.append(prompt)

        return kshot_prompt, prompted_test_examples, test_dataset[label_column]

    @staticmethod
    def prepare_chat_completion_prompts(prompted_test_examples, task):
        temp_prompt_texts=prompted_test_examples

        system_to_replace={
            'sentiment':'Instruction:\n',
            'nli':'Instruction: ',
            'sib':'Instruction:\n',
            'belebele':'Instruction:\n',
            'sdqa':'Instruction:\n',
            'udp': 'Instruction:\n',
            'pos': 'Instruction:\n',
            'ner': 'Instruction:\n'
        }
        user_to_replace={
            'sentiment':'Sentence: ',
            'nli':'Relationship: ',
            'sib':'Sentence: ',
            'belebele':'',
            'sdqa':'',
            'udp':'Input:\n',
            'pos':'Input:\n',
            'ner': 'Input:\n'
        }
        assistant_to_replace={
            'sentiment':'Sentiment: ',
            'nli':'',
            'sib':'Topic: ',
            'belebele':'',
            'sdqa':'',
            'udp':'Output:\n',
            'pos':'Output:\n',
            'ner': 'Output:\n'
        }


        new_prompts=[]
        for prompt_text in temp_prompt_texts:
            data=prompt_text.split('\n\n')
            result = []
            # Add the first item as the system prompt
            result.append({"role": "system", "content": data[0].replace(system_to_replace[task],'')})

            # Process the remaining items
            for i in range(1, len(data)):
                item = data[i]
                if task=='nli':
                    parts=item.split('\nRelationship: ')
                    # Last item: add only the user question
                    if i == len(data) - 1:
                        result.append({"role": "user", "content": parts[0]})
                    else:
                        result.append({"role": "user", "content": parts[0]})
                        result.append({"role": "assistant", "content": parts[1]})
                elif task=='belebele' or task=='sdqa':
                    parts=item.split('Answer: ')
                    # Last item: add only the user question
                    if i == len(data) - 1:
                        result.append({"role": "user", "content": parts[0]})
                    else:
                        result.append({"role": "user", "content": parts[0]})
                        result.append({"role": "assistant", "content": parts[1]})
                elif task=='udp' or task=='pos' or task=='ner':
                    parts = item.split('Output:\n')
                    if i == len(data) - 1:
                        # Last item: add only the user question
                        result.append({"role": "user", "content": parts[0].replace(user_to_replace[task],'').strip()})
                    else:
                        # Other items: add user question and assistant response
                        result.append({"role": "user", "content": parts[0].replace(user_to_replace[task],'').strip()})
                        result.append({"role": "assistant", "content": parts[1].replace(assistant_to_replace[task],'').strip()})
                else:
                    parts = item.split('\n')

                    if i == len(data) - 1:
                        # Last item: add only the user question
                        result.append({"role": "user", "content": parts[0].replace(user_to_replace[task],'')})
                    else:
                        # Other items: add user question and assistant response
                        result.append({"role": "user", "content": parts[0].replace(user_to_replace[task],'')})
                        result.append({"role": "assistant", "content": parts[1].replace(assistant_to_replace[task],'')})

            new_prompts.append(result)
        return new_prompts