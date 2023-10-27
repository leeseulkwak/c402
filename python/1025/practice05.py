numbers=[1,2,5,3,3,2,3,4,5,4,5,6,2,3,4,3,1,2,7,8,6,9]
counter={}

for number in numbers:
    if number in counter:
        counter[number]=counter[number]+1
    else:
        counter[number]=1
    
print(counter)