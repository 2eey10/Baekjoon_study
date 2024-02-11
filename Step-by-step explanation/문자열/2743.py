import sys

while True:
    a = sys.stdin.readline()
    while a.isupper() == True or a.islower() == True:
        print(len(a)-1)
        break
    break

    
