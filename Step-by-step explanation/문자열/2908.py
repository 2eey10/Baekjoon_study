import sys

a, b = map(str, sys.stdin.readline().split())

# 주어진 수를 거꾸로 정렬
a, b = int(a[::-1]), int(b[::-1])
list = [a, b]

print(max(list))
