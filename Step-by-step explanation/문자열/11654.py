#ASCII CODE

a = input()
if a.isupper() or a.islower() or 0<= int(a) <= 9:
    print(ord(a))