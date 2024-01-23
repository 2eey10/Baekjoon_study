import sys
t = int(input())
cnt = 1

for i in range(t):
    a , b = map(int, sys.stdin.readline().split())
    while 0< a< 10 and 0 < b < 10:
        print(f"Case #{cnt}: {a} + {b} =", a+b)
        cnt += 1
        break

    