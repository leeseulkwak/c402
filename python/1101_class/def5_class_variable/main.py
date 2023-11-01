from Calculator import Calculator
from History import History

if __name__ == "__main__":
    # 사용자로부터 값을 입력받음
    a = float(input("첫 번째 숫자를 입력하세요: "))
    b = float(input("두 번째 숫자를 입력하세요: "))

calc1=Calculator()

result=calc1.add(a,b)
print(f"{a}+{b}={result}")
Calculator.add_entry(a,b,'+',result)

calc2 = Calculator()

result = calc2.subtract(a, b)
print(f"{a} - {b} = {result}")
Calculator.add_entry(a, b, '-', result)

calc3 = Calculator()

result = calc3.multiply(a, b)
print(f"{a} x {b} = {result}")
Calculator.add_entry(a, b, 'x', result)

calc4 = Calculator()

result = calc4.divide(a, b)
print(f"{a} / {b} = {result}")
Calculator.add_entry(a, b, '/', result)

print("\n--- History ---")
Calculator.display()

