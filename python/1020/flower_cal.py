
#거리구하기
def dist(a, b):
    d=((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    return d

#거리를 리스트로 반환
def dist_list(s, t):
    d_list=[]
    for i in s:
        d=dist(i, t)
        d_list.append(d)
    return d_list

#작은 값부터 정렬
def sort(lst):
    sorted_lst=sorted(enumerate(lst), key=lambda x:x[1])
    sorted_idx=[index for index, value in sorted_lst]
    return sorted_idx

if __name__=='__main__':
    src=[[5.1,3.5], [4.9,3.0], [6.0,3.0], [6.2, 2.8], 
            [5.5,2.3], [6.3,3.3], [5.8,2.7], [6.7,3.0]]

    trg=[5.4,3.2]
    
    dists=dist_list(src, trg)
    print(dists)

    top3=sort(dists)
    print(top3)
