
import sys

array = []

for i in range(9):
    n = int(sys.stdin.readline())
    if 0 < n < 100:
        array.append(n)

print(max(array))
print(array.index(max(array))+1)
