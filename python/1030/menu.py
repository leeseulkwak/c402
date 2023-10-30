


while True:
    try: #예외가 발생 할 수 있는 곳
        text="""
    메뉴
    1- 한식
    2- 중식
    3- 일식
    4- 분식
    """
        print(text)
        choice=input("메뉴를 선택해주세요.>")
        if choice=="1":
            print("한식입니다.")
        elif choice=="2":
            print("중식입니다.")
        elif choice=="3":
            print("일식입니다.")
        elif choice=="4":
            print("분식입니다.")
        elif choice=="9":
            break
        else:
            print("메뉴를다시선택")
        # if choice not in ["1", "2", "3", "4", "9"]:
        #     raise
    except:
        print("메뉴를 다시 선택해 주세요")