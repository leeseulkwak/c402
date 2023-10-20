def selection_sort(arr):
    for i in range(len(arr)):
        # 가장 작은 요소의 인덱스를 찾는다.
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # i번째 요소와 min_index 요소를 교환한다.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = selection_sort(lst)
print(sorted_lst)  # [11, 12, 22, 25, 34, 64, 90]
