class DNode:
    def __init__(self, data, prev, next): 
        self.data = data 
        self.prev = prev
        self.next = next 
     
class DlistType:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFront(self,data):
        node = DNode(data, None, self.front)

        if self.isEmpty():
            self.front = self.rear = node
        else:
            #self.front = node
            self.front.prev = node
            self.front = node #순서를 바꿔주는 이유? front 이후 노드들의 주소 때문에

        self.size += 1

    def addRear(self,data):
        node = DNode(data, self.rear, None)

        if self.isEmpty():
            self.front = self.rear = node
        else:
            #self.front = node
            self.rear.next = node
            self.rear = node #순서를 바꿔주는 이유? front 이후 노드들의 주소 때문에

        self.size += 1

    def add(self, pos, data):
        node = DNode(data, None, None) #아직 결정이 안 됐다. 여기서의 None은 없다가 아님

        if pos == 1:
            self.addFront(data)
        elif pos == self.size +1:
            self.addRear(data)
        else:
            p = self.front

            for i in range(i, pos):
                p = p.next
                
                node.prev = p.prev
                node.next = p
                p.prev.next = node
                p.next = node

        self.size += 1


    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data

    def display(self):
        p = self.front      #p:link 화살표

        while p != None:
            print('[%s] -> ' % p.data, end ='')
            p = p.next # 다음 노드로 이동
        print('\b\b\b   ') #화살표 없애기

if __name__ == "__main__":
    DL = DlistType()

    DL.addFront('A')
    DL.addFront('C')
    DL.addFront('D')
    DL.display() 

    DL.addRear('E')
    DL.display()
    DL.deleteFront()
    DL.display()
    DL.deleteRear()
    DL.display()