dict={
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["100", "설탕", "메타중아황산나트륨"],
    "origin": "필리핀"
}

print(dict["name"])
print(dict["type"])
print(dict["ingredient"])
print(dict["origin"])

dict["name"]="8D 건조 망고"
print(dict["name"])

dict["price"] = 5000
print(dict)

del dict["ingredient"]

print(dict)