from Calculator import Calculator
from History import History

if __name__ == "__main__":
    # 사용자로부터 값을 입력받음
    a = float(input("첫 번째 숫자를 입력하세요: "))
    b = float(input("두 번째 숫자를 입력하세요: "))

calc=Calculator()
history=History()

result=calc.add(a,b)
print(f"{a}+{b}={result}")
history.add_entry(a,b, '+', result)

result=calc.subtract(a,b)
print(f"{a}-{b}={result}")
history.add_entry(a,b, '-', result)

result=calc.multiply(a,b)
print(f"{a}*{b}={result}")
history.add_entry(a,b, '*', result)

result=calc.divide(a,b)
print(f"{a}/{b}={result}")
history.add_entry(a,b, '/', result)

print("\n--- History ---")
history.dispaly()
