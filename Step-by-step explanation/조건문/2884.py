def time_interval(x, y):
    if x != 0:
        if y > 45:
            y= y- 45
            return x, y
        elif y == 45:
            y = 0
            return x, y 
        else:
            y = y + 60 -45
            x = x - 1
            return x, y
    else:
        if y > 45:
            x = 0
            y= y- 45
            return x, y
        elif y == 45:
            y = 0
            return x, y
        else:
            y = y + 60 -45
            x = 23
            return x, y

while True:
    a, b = map(int, input().split())
    if (0 <= a <= 23) and (0 <= b <= 59):
        break

x, y = time_interval(a,b)
print(x, y)
    

