def mul(*values):
    output=1
    for value in values:
        output*=value
    return output

print(mul(5,7,9,10))