import sys
t = int(input())

cnt = 0
while cnt < t:
    r, p = map(str, sys.stdin.readline().split()) 
    r = int(r)

    for i in p:
        print(r*i, end="")
    print()
    cnt += 1
    



