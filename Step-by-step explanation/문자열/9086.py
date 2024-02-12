t = int(input())
cnt = 0
if 1 <= t <= 10:
    while cnt < t:
        a  = str(input())
        if a.isupper() and len(a) < 1000:    
            print(a[0] + a[-1])
        cnt += 1
        
    