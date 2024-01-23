def factorial(n):
    res = 0
    while n > 0:
        res += n
        n -= 1
    return res

n = int(input())
if 1 <= n <= 10000:
    result = factorial(n)            
    print(result)
else:
    print("None")
