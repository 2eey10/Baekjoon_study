class Node:
    def __init__(self, data, next = None): #next = 다음링크
        self.data = data #데이터 필드
        self.next = next #다음 노드 주소

class QueueType:
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.tail == None
    
    def enqueue(self,data): #insertLast(), rear에서 삽입되는 것
        node = Node(data)

        if self.isEmpty():
            node.next = node #난 누굴 가르키지? -> 자신을 가리킴
            self.tail = node #날 누가 가르키지? -> isEmpty()인 상황에서 마지막 노드
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node

        self.size += 1

    def insertFirst(self,data): #insertLast와 다른 점: self.tail = node이 없음
        node = Node(data)

        if self.isEmpty():
            node.next = node #난 누굴 가르키지? -> 자신을 가리킴
            self.tail = node #날 누가 가르키지? -> isEmpty()인 상황에서 마지막 노드
        else:
            
            node.next = self.tail.next #순서
            self.tail.next = node #잘 지킬 것
            #self.tail = node

        self.size += 1

    def dequeue(self): #deletefirst
        if not self.isEmpty():
            p = self.tail
            q = p.next

            data = q.data
            if p == q: #node가 하나라면 두 개의 화살표 p,q가 같은 지점을 가리킬 것
                self.tail = None
            else:    
                p.next = q.next
            self.size -= 1
            return data
        else:
            pass
    def get_size(self): #size() 함수. 위 인스턴스 변수 size와 구분짓기 위해 get_size()로 
        node = self.tail.next
        count = 1
        while not node == self.tail:
            node = node.next
            count += 1
        return count
    
    def display(self):
        if not self.isEmpty():
            p = self.tail.next
            for i in range(self.size):
                print('[%s] -> '%p.data, end='')
                p = p.next
            print('\b\b\b     ')
        else: pass

if __name__ =='__main__':
    Q = QueueType()
    Q.enqueue('A')
    Q.display()
    Q.enqueue('B')
    Q.display()
    Q.enqueue('C')
    Q.display()
    Q.enqueue('D')

    Q.insertFirst('F')
    Q.display()
    print((Q.get_size()))
    Q.dequeue()
    Q.display()