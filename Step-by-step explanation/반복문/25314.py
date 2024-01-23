n = int(input())
while (n <= 1000) and ((n % 4) == 0):
    a  = n // 4
    for i in range(a):
        res = ("long"  + " ")* a + "int"
    print(res)
    break

