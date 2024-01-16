a, b = map(int, input().split())

def tkclr(op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b 
    elif op == "*":
        return a * b
    elif op == "//":
        return a // b
    elif op == "%":
        return a % b

myList = ["+", "-", "*", "//", "%"]
for i in myList:
    print(tkclr(i))
