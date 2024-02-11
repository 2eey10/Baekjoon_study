import sys

while True:
    a = sys.stdin.readline().strip()
    while a.isupper() or a.islower():
        print(len(a))
        break


    
