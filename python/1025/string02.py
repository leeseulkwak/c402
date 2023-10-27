number=int(input("정수입력>"))

if number % 2==0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는 짝수입니다."
    ]).format(number, number))
else:
    print((
        "엽락한 문자열은 {}입니다.\n"
        "{}는 홀수입니다."
    ).format(number, number))