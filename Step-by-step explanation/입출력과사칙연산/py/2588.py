
a = int(input())
b = int(input())


def digit_mul(num_a, num_b, n):
    num_b = list(str(num_b))
    digit_num = num_b[n-1]
    digit_num = int(digit_num)
    return num_a * digit_num


for i in range(3,0,-1):
    print(digit_mul(a, b, i))
print(a*b)
    


