from ArrayStack import ArrayStack

map = [ ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '0', '0', 'x'], 
        ['1', '1', '1', '0', '1', '1'],
        ['1', '1', '1', '1', '1', '1']]

SIZE = 6

def isValidPos(r,c):
    if 0 <= r < SIZE and 0 <= c <SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True

    return False

#깊이우선탐색

def DFS():
    print('DFS: ')
    S = ArrayStack(100)

    S.push((1,0)) #

    while not S.isEmpty():
        pos = S.pop()
        print(pos, end ='->')
        (r,c) = pos

        if(map[r][c] == 'x'):
            return True
        else:
            map[r][c] = '.' #r행에 c열. 위치 방문함. '.'표시


            if isValidPos(r-1,c): S.push((r-1,c))
            if isValidPos(r+1,c): S.push((r+1,c))
            if isValidPos(r,c-1): S.push((r,c-1))
            if isValidPos(r,c+1): S.push((r,c+1))

        S.display()
    return False

result = DFS()

if result:
    print('Success')
else:
    print('Fail')

    


