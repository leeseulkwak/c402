
lst=["A", "B", "C", "D", "A"]
new_list=[]

def output(list):
    for value in list:
     if value not in new_list:
        new_list.append(value)
        
    return new_list
    
print(output(lst))
# if __name__=='__main__':
    