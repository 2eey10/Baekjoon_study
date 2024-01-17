N = 100

class Maxheap:
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0 #힙사이즈: 노드의 번호 및 힙 내 노드의 개수 및 마지막 노드

    def upHeap(self):
        idx = self.heapSize #가장 최근 들어온 노드의 인덱스번호
        item = self.heap[idx] # 가장 최근 들어온 값

        while (idx != 1 and item > self.heap[idx // 2]): #루트노드가 아니고 부모노드 크기비교
            self.heap[idx] = self.heap[idx//2]
            idx //= 2 #인덱스 계속 2로 나눠주기 -> 결국 인덱스 1로 됨

        self.heap[idx] = item   #인덱스가 1이 되면, 노드 번호 1번 자리에 해당 item 삽입

    def insertItem(self, item):
        self.heapSize += 1 #삽입하려면 먼저 1 증가
        self.heap[self.heapSize] = item
        self.upHeap()

    def display(self):
        print('Heap: ', self.heap[1:self.heapSize + 1])

    def downHeap(self): 
        item = self.heap[1] #루트노드에 올라온 요소 저장
        parent = 1 #부모노드
        child = 2 

        while child < self.heapSize:
            if (child < self.heapSize) and (self.heap[child+1 > self.heap[child]]):      #(1)오른쪽 형제 노드가 있다면, 왼쪽과 오른쪽 비교
                child += 1

            if item >= self.heap[child]:
                break

            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2

        self.heap[parent] = item

    def deleteItem(self): #루트노드 삭제
        item = self.heap[1] 

        self.heap[1] = self.heap[self.heapSize] #루트노드를 맨 마지막으로 내리기
        self.heapSize -= 1
        self.downHeap()
        return item

    


if __name__ == "__main__":
    H = Maxheap()
    data = [7,5,3,9,4,6,2,2,1,3]
    
    for i in data:
        H.insertItem(i)
        H.display()
        print()
        ##H.insertItem(8); H.display()

        print('[%d] is deleted' % H.deleteItem())
        H.display()
