def compute_uas_las(output, true_deprels, true_heads):
    # Parse the output
    predictions = []
    for line in output.strip().split("\n"):
        _, _, _, pred_deprel, pred_head = line.split()
        predictions.append((int(pred_head), pred_deprel))
    
    # Compare predictions with ground truth
    correct_heads = 0
    correct_deprels = 0
    total = len(predictions)
    
    for i, (pred_head, pred_deprel) in enumerate(predictions):
        if pred_head == true_heads[i]:
            correct_heads += 1
            if pred_deprel == true_deprels[i]:
                correct_deprels += 1
    
    # Compute UAS and LAS
    uas = correct_heads / total
    las = correct_deprels / total
    
    return uas, las

def eval_result_sa(all_preds,all_true_labels,choices):
    count=0
    ind_true=[]
    not_true=[]
    indx=[]
    choices=[str(x).lower() for x in choices]
    for i,res in enumerate(all_preds):
        if res in choices:
            if str(res).lower()==str(all_true_labels[i]).lower():
                count+=1
                ind_true.append(i)
            else:
                not_true.append(i)
                indx.append(res)
    acc=count/len(all_preds)
    # print(acc, count, len(all_preds), len(all_true_labels), not_true,indx)
    return 



def compute_accuracy(all_preds, all_true_labels, choices):
    all_true_labels=[str(x).lower() for x in all_true_labels]
    all_preds=[str(x).lower() for x in all_preds]
    choices = [str(x).lower() for x in choices]

    correct_predictions = sum(p == t for p, t in zip(all_preds, all_true_labels))
    total_predictions = len(all_preds)
    
    accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
    
    # Compute per-class accuracy
    class_accuracies = {}
    for choice in choices:
        class_true = sum(t == choice for t in all_true_labels)
        class_correct = sum((p == t == choice) for p, t in zip(all_preds, all_true_labels))
        class_accuracies[choice] = class_correct / class_true if class_true > 0 else 0

    return accuracy
# def compute_f1(all_preds, all_true_labels, choices,task='nli'):
#     true_positives = 0
#     false_positives = 0
#     false_negatives = 0
    
#     choices = [str(x).lower() for x in choices]
    
#     for pred, true_label in zip(all_preds, all_true_labels):
#         pred=str(pred).lower()
#         true_label=str(true_label).lower()
#         if task=='mrc':
#             pred=pred.replace('.','')
#         if pred in choices:
#             if pred == true_label:
#                 true_positives += 1
#             else:
#                 false_positives += 1
#         elif str(true_label) in choices:
#             false_negatives += 1
    
#     precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
#     recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    
#     f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
#     return f1


def compute_f1(all_preds, all_true_labels, choices, task='nli'):
    def calculate_class_f1(true_class, pred_class):
        true_positives = sum(pred_class in true_set for true_set, pred in zip(all_true_labels, all_preds) if pred == pred_class)
        false_positives = sum(pred == pred_class and pred not in true_set for true_set, pred in zip(all_true_labels, all_preds))
        false_negatives = sum(true_class in true_set and pred != true_class for true_set, pred in zip(all_true_labels, all_preds))
        
        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
        
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        return f1

    # Normalize all inputs
    all_true_labels = [str(x).lower() for x in all_true_labels]
    all_preds = [str(x).lower() for x in all_preds]
    choices = [str(x).lower() for x in choices]
    if task == 'mrc':
        all_preds = [x.replace('.', '') for x in all_preds]
        all_true_labels = [[x.replace('.', '') for x in true_set] for true_set in all_true_labels]

    class_f1_scores = {choice: calculate_class_f1(choice, choice) for choice in choices}
    
    macro_f1 = sum(class_f1_scores.values()) / len(choices)
    
    return macro_f1

def compute_f1_multi_reference(all_preds, all_true_labels, task='qa'):
    def calculate_f1(pred, true_set):
        if pred is None:
            pred = ""  # Treat None as an empty string
        else:
            pred = str(pred).lower()  # Convert to string and lowercase
        
        true_set = [str(t).lower() for t in true_set]  # Convert all true labels to lowercase strings
        
        if task == 'mrc':
            pred = pred.replace('.', '')
            true_set = [t.replace('.', '') for t in true_set]

        if pred in true_set:
            precision = 1.0
            recall = 1.0
        else:
            precision = 0.0
            recall = 0.0

        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        return f1

    f1_scores = [calculate_f1(pred, true_set) for pred, true_set in zip(all_preds, all_true_labels)]
    macro_f1 = sum(f1_scores) / len(f1_scores)
    
    return macro_f1