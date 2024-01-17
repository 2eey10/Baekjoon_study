class CircularQUeue:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.queue = [None] * self.capacity #빈값으로 채워진 배열
        self.front = self.rear =0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity #포화상태
    
    def enqueue(self,e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e
        else:
            print('FULL')

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front +1) % self.capacity
            return self.queue[self.front]
        
        else:
            print('EMPTY')

    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front +1) % self.capacity]
        
        else:
            print('EMPTY')

    def display(self):
        print('Front : %d, Rear : %d' %(self.front, self.rear))

        i = self.front
        #dowhile문 형식식
        while i != self.rear : #front != rear 라면
            i = (i+1) % self.capacity
            print('[%c]' % self.queue[i], end=' ')
        print()

if __name__ == '__main__':
    Q = CircularQUeue()
    Q.enqueue('A'); Q.enqueue('B');Q.enqueue('C');
    Q.enqueue('D');Q.enqueue('E');Q.display()    
    
    print('Dequeue --> ', Q.dequeue())
    print('Dequeue --> ', Q.dequeue())
    print('Dequeue --> ', Q.dequeue())
    Q.display()

    Q.enqueue('A')
    Q.enqueue('B')
    Q.enqueue('C')
    Q.display()
