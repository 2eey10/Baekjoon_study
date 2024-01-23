x = int(input())
n = int(input())

if (1 <= x <= 1000000000) and (1 <= n <= 100):
    cnt = 0
    prs = 0
    while cnt < n:
            a, b = map(int, input().split())
            if (1 <= a <= 1000000) and (1 <= b <= 10):
                prs += a * b
                cnt += 1

    if x == prs:
        print("Yes")
    else:
        print("No")
else:
    print("Invalid input. Please enter valid values for x and n.")
