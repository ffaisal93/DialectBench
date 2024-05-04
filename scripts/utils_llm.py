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

def eval_result(all_preds,all_true_labels):
    count=0
    ind_true=[]
    not_true=[]
    indx=[]
    for i,res in enumerate(all_preds):
        if res in choices:
            if choices.index(res)==all_true_labels[i]:
                count+=1
                ind_true.append(i)
            else:
                not_true.append(i)
                indx.append(res)
    acc=count/len(all_preds)
    # print(acc, count, len(all_preds), len(all_true_labels), not_true,indx)
    return acc