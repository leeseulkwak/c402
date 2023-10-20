def precision(y_true, y_pred): #정밀도 계산 함수
    #y_true: 실제 라벨 테스트
    #y_pred: 모델이 예측한 라벨 리스트

    zip_list=[]
    TP=[]
    FP=[]

    for i in range(len(y_true)):
        lst=[]
        lst.append(y_true[i])
        lst.append(y_pred[i])
        zip_list.append(lst)

    for j in range(len(zip_list)):
        if zip_list[j][0] == 1 and zip_list[j][1] ==1:
            TP.append(0)
        else:
            zip_list[j][0] == 0 and zip_list[j][1] ==1
            FP.append(0)
        

    return TP / (TP+FP)

y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 1, 0, 1, 0, 1, 1]

print(precision(y_true, y_pred))
 