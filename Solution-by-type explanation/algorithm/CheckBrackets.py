from ArrayStack import ArrayStack

def checkBrackets(str):
    S = ArrayStack()

    for c in str:
        if c == '[' or c == '{' or c == '(':
            S.push(c)
        elif c == ']' or c == '}' or c == ')': 
            if S.isEmpty(): ## 조건2 위배
                return False
            else:
                left = S.pop()

                if (c == ']' and left != '[') or \
                   (c == '}' and left != '{') or \
                   (c == ')' and left != '('):
                    return False
                
                
                
    return S.isEmpty()

s1 = "{ A [ (i+1) ] = 0; }"
s2 = "if( (i==0) && (j==0)"
s3 = "A[ ( i+1] ) = 0;"
s4 = "a d r g h"
s5 = ""

print(s1, " --->", checkBrackets(s1))
print(s2, " --->", checkBrackets(s2))
print(s3, " --->", checkBrackets(s3))
print(s4, " --->", checkBrackets(s4))
print(s5, " --->", checkBrackets(s5))