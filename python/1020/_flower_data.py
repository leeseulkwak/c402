#딕셔너리를 선언

dictionary={
    'flower_length' : '5.1', 
    'flower_width' : '3.5'
    # "flower_type" : ["세토사", "세토사", "베르시컬러", "베르시컬러", "베르시컬러", "세토사", "베르시컬러", "세토사"]
}


length=dictionary.get('flower_length')
width=dictionary.get('flower_width')

x=float(length)
y=float(width)

print(x,y)

