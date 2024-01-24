import sys
n, x = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))

k = []
for i in range(n):
    if x > a[i]:
        k.append(a[i])

for i in k:
    print(i, end=" ")
