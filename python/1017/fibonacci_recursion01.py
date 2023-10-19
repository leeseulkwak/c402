def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else : 
        return fibonacci(n-1)+fibonacci(n-2)
       
print("피보나치(1): ", fibonacci(1))
print("피보나치(2): ", fibonacci(2))
print("피보나치(3): ", fibonacci(3))
print("피보나치(4): ", fibonacci(4))
print("피보나치(5): ", fibonacci(5))
print("피보나치(6): ", fibonacci(6))