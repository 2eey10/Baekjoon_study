n = str(input())

def dial_time(ch):
    if ch in 'ABC':
        return 3
    elif ch in 'DEF':
        return 4
    elif ch in 'GHI':
        return 5
    elif ch in 'JKL':
        return 6
    elif ch in 'MNO':
        return 7
    elif ch in 'PQRS':
        return 8
    elif ch in 'TUV':
        return 9
    elif ch in 'WXYZ':
        return 10
    else:
        return 0

if n.isupper() and 2 <= len(n) <= 15:
    result = sum(dial_time(char) for char in n)
    print(result)
