

def merge_sort(arr):
    if len(arr)<=1:  #기본 조건 : 원소의 수가 1 이하이면 정렬할 필요가 없다.
        return arr
    #1. 분할단계
    mid=len(arr)
    left=arr[:mid]
    right=arr[mid:]

    #2.정복단계(재귀적으로 병합 정렬을 호출)
    left=merge_sort(left)
    right=merge_sort(right)


    #3.병합단계
    return merge(left, right)


def merge(left, right):
    result=[]
    i=j=0

    #left와 right의 원소를 비교하여 작은 원소부터 result에 추가
    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    #남아 있는 원소들은 result에 추가
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1

    return result

if __name__=='__main__':
    #예제
    arr=[5, 10, 1, 2, 9, 8]
    sorted_arr=merge_sort(arr)
    print(sorted_arr)