# Calculator.py
class Calculator:

 #데코레이터 : 인스턴스 메소드와는 다르게 self 인자 없음
 #클래스 이름으로 직접 메소드 호출 가능
 #인스턴스 속성세 접근 하거나 인스턴스 메소드를 호출 할 수 없다.
#클래스 안에 함수를 사용하면 메소드가 됨

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Division by zero is not allowed"
        return a / b

