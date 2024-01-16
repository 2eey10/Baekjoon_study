def square_money(x, y, z):
    if (x == y == z):
        return 10000 + (x * 1000)
    elif ((x == y) and (x != z)):
        return 1000 +(x * 100) 
    elif ((y == z) and (y != x)):
        return 1000 +(y * 100) 
    elif ((z == x) and (z != y)):
        return 1000 +(z * 100)
    else:
        d = max(x,y,z)
        return d * 100
         


while True:
    a, b, c = map(int, input().split())
    if (1<= a <= 6) and (1<= b <= 6) and (1<= c <= 6):
        break
 
res = square_money(a, b, c)
print(res)