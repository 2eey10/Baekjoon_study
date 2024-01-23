class ArrayStack:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.stack = [None] * self.capacity #stack:배열이름
        self.top = -1


    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity -1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('Overflow!')
    
    def pop(self):
        if not self.isEmpty():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print('Empty!')

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print('Empty!')

    def sortedPush(self,e):
        if self.isEmpty() or e > self.peek(): #비어있을떄
            self.push(e)
        else:
            tmp = ArrayStack(self.capacity)
            while not self.isEmpty() and e < self.peek():
                tmp.push(self.pop())

            self.push(e) 
            
            while not tmp.isEmpty():
                self.push(tmp.pop())        #스택이기 때문에 기존에걸 pop 하고 처리 해야함. 

    def size(self):
        return self.top + 1
    
    def display(self):
        print(self.stack[0: self.top + 1]) #꼭대기부터 0번인덱스까지

if __name__ == '__main__':
    S = ArrayStack()
    
    data = [5, 3, 8, 1, 2, 7]
    S.isEmpty()
    #str = input('Input a string : ')
    for i in range(1,101):
        S.push(i)
    S.pop()
    S.push(100)
    S.isEmpty()
#    S.push(101) #overflow!
#    S.display()
    
    print(S.size())
    print(S.isFull())
    print(S.isEmpty())
    for d in data:
        S.sortedPush(d)
        S.display()
    
# 5
# 3 5
# 3 5 8
# 1 3 5 8
# 1 2 3 5 8 




    print('After Pop: %c' % S.pop())

    S.display()
    
    print('After Peek: %c' % S.peek())

    S.display()

    #while not S.isEmpty():
        #print(S.pop(), end = '')







        