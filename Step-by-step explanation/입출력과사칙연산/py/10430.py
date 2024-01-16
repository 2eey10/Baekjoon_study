a, b ,c = map(int, input().split())

def deviding(x,y, z):
    l1 = (x + y) % z;
    l2 = ((x%z) + (y+z)) % z;
    l3 = (x*y) % z;
    l4 = ((x%z) * (y%z)) % z;
    return  l1, l2, l3, l4

result = deviding(a,b,c)
for i in result:
    print(i)