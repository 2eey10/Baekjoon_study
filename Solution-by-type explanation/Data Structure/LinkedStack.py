class Node:
    def __init__(self, data, next): #next = 다음링크
        self.data = data #데이터 필드
        self.next = next #다음 노드 주소

class StackType:
    def __init__(self):
        self.top = None #'아무 노드도 연결돼있지 않다'로 초기화
        self.size = 0

    def isEmpty(self):
        return self.top == None
        #return self.size == 0 둘 중 아무거나 활성화 시키기

    def clear(self):
        self.top = None

    def push(self, data): #insertFirst(): 첫번째로 삽입
        node = Node(data,self.top) #객체 생성. #첫번째 노드 포인터로 가리키기
        self.top = node #자신을 top포인터로 가리키기 -> 첫번째 노드화
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            p =  self.top #top을 p 포인터로 가리키기 = p
            self.top = p.next # top이 p 다음을 가리키도록
            self.size -= 1
            return p.data 
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.top.data
        
        else: pass

    def get_size(self): #size() 함수. 위 인스턴스 변수 size와 구분짓기 위해 get_size()로 
        node = self.top
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count


    def display(self):
        p = self.top      #p:link 화살표

        while p != None:
            
            print('[%s] -> ' % p.data, end ='')
            p = p.next # 다음 노드로 이동
        print('\b\b\b   ') #화살표 없애기
    




if __name__ == "__main__":
    S = StackType()
    S.push('B')
    S.push('A')
    S.push('C')
    S.push('D')
    S.display()
    S.pop()
    print(S.get_size())
    S.display()
#    print('pop : %s' % S.pop(); S.display())

