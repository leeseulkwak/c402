
def factorial2(n):

    if n ==0:
        return 1
    else:
        return n * factorial2(n-1)
    
print("5!:", factorial2(5))


def factorial3(n, s=1):
    if n==0:
        return 1
    if s==n:
        return s
    return s * factorial3(n, s+1)

print(factorial3(5))