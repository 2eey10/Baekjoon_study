n = int(input())
while 1<= n <= 100:
    for i in range(n):
        print((" " * (n-i-1)) + ("*" * (i+1)))
    break

