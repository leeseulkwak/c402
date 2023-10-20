

#  correct = sum(true == pred for true, pred in zip(y_true, y_pred)) return correct / len(y_true)

def accuracy(y_true, y_pred):

    zip_list=[]
    correct_list=[]
    for i in range(len(y_true)):
        lst=[]
        lst.append(y_true[i])
        lst.append(y_pred[i])
        zip_list.append(lst)

    for j in range(len(zip_list)):
        if zip_list[j][0] == zip_list[j][1]:
            correct_list.append(1)
        else:
            correct_list.append(0)
    correct=sum(correct_list)

    return correct / len(y_true)


y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 0]

print(accuracy(y_true, y_pred))
 