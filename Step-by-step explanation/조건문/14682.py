def quadrant(x, y):
    if (x > 0) and (y > 0):
        return 1 
    elif (x < 0) and (y > 0):
        return 2
    elif (x < 0) and (y < 0):
        return 3
    else:
        return 4

while True:
    a = int(input())
    b = int(input())
    
    if ((-1000 <= a <= 1000) and (-1000 <= b <= 1000)) and ((a != 0) and (b != 0)):
        break

res = quadrant(a, b)
print(res)
