import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

array = []

for i in range(n):
    array.append(a[i])

x = max(array)
y = min(array)

print(y,x, end=" ")