books=[{
    "제목" : "혼자 공부하는 파이썬",
    "가격" : 27000
}, {
    "제목" : "혼자 공부하는 머신러닝 + 딥러닝", 
    "가격" : 26000
}]

books.sort(key=lambda book: book["가격"])
for book in books:
    print(book)