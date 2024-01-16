while True:

    year = int(input())
    if 1 <= year <= 4000:
        def near_year(year):
            if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 400 == 0)):
                return 1
            else:
                return 0
        break

res = near_year(year)
print(res)
    
