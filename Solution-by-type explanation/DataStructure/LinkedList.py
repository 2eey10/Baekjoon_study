class Node:
    def __init__(self, data, next): #next = 다음링크
        self.data = data #데이터 필드
        self.next = next #다음 노드 주소

class ListType:
    def __init__(self):
        self.head = None #'아무 노드도 연결돼있지 않다'로 초기화
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def getNode(self,pos): ##pos가 가리키는 노드의 이전 노드 위치를 찾기
        p = self.head 

        if pos == 1: ##1인 경우는 주소를 나타내는 이전 노드가 존재하지 않는다
            return None ## pos 값은 1부터. 위치니깐.
        else:
            while pos > 2:
                p = p.next 
                pos -= 1  
            return p #p는 pos의 이전 노드를 가리키고 있음.  


    def insert(self,pos,data):
        before = self.getNode(pos) #before = pos 이전 노드

        if before == None:
            self.head = Node(data,self.head) #노드 생성

        else:
            node = Node(data, before.next)
            before.next = node
        self.size += 1

    def delete(self,pos):
        before = self.getNode(pos)
        
        if before == None:
            if(not self.isEmpty()):
                self.head = self.next #두번째노드가 첫번째 노드가 된다

        else:
            before.next = before.next.next
        self.size -= 1


    def display(self):
        p = self.head      #p:link 화살표

        while p != None:
            print('[%s] -> ' % p.data, end ='')
            p = p.next # 다음 노드로 이동
        print('\b\b\b   ') #화살표 없애기

if __name__ == "__main__":
    L = ListType()

    L.insert(1,"A")
    L.insert(1,"B")
    L.insert(L.size + 1,"C")
    L.display()


    L.delete(2)
    L.display()