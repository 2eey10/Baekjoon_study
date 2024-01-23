from CircularQueue import CircularQUeue

class CircularDeque(CircularQUeue):
    def __init__(self, capacity= 10):
        super().__init__(capacity)              
    #자식클래스 객체 생성 전에 부모클래스 객체 생성 먼저 해야함
    #isEmpty(), isFull(), display()는 그냥 사용한다

    def addFront(self, e):
        if not self.isFull():
            self.queue[self.front] = e #요소 삽입
            self.front = (self.front -1 + self.capacity) % self.capacity #반시계방향회전
        else: pass
    
    def addRear(self, e):
        self.enqueue(e)

    def deleteFront(self):
        self.dequeue()

    def deleteRear(self):
        if not self.isEmpty():
            e = self.queue[self.rear]
            self.rear = (self.rear -1 + self.capacity) % self.capacity
            return e
        else: pass
    
    def getFront(self):
        self.peek()

    def getRear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
            
        else: pass

if __name__ == "__main__":
    import random

    D = CircularDeque()
    for i in range(4):
        D.addFront(random.randint(65,90))
    D.display() #7890

    for i in range(3):
        D.addRear(random.randint(65,90))
    D.display() #7890123

    for i in range(2):
        D.deleteFront()
    D.display() 

    for i in range(3):
        D.deleteRear()
    D.display() 

