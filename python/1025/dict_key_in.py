dict={
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["100", "설탕", "메타중아황산나트륨"],
    "origin": "필리핀"
}

key=input("접근하고자하는 키\n")

if key in dict:
    print(dict[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")