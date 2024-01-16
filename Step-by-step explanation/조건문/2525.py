def oven_time_interval(a, b, c):
    c_a, c_b = c // 60, c % 60 
    hour_hap = a + c_a
    min_hap = b + c_b

    if min_hap >= 60:
        hour_hap = hour_hap + 1
        min_hap = min_hap % 60
        if hour_hap >= 24:
            hour_hap = hour_hap % 24
            return hour_hap, min_hap
        else:
            return hour_hap, min_hap
    else:
        min_hap = min_hap
        if hour_hap >= 24:
            hour_hap = hour_hap % 24
            return hour_hap, min_hap
        else:
            return hour_hap, min_hap

    
     

while True:
    a, b = map(int, input().split())
    c = int(input())
    if ((0 <= a <= 23) and (0 <= b <= 59)) and (0 <= c <= 1000):
        break

h, m = oven_time_interval(a, b, c)
print(h, m)

