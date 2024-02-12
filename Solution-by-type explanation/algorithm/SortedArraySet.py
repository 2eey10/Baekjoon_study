class SortedArraySet:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def __str__(self):
        return str(self.array[0:self.size])
    
    def contains(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    def insert(self,e):
        if self.contains(e) or self.isFull():
            return     #아무것도 하지마
        
        self.array[self.size] = e
        self.size += 1

        for i in range(self.size-1, 0, -1): #역으로 탐색
            if self.array[i-1] <= self.array[i]: #왼쪽원소(앞의원소)
                break
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1]
    def delete(self, e):
        if not self.contains(e): #e가 존재하지 않으면
            return  #아무 일도 일어나지 않는다
        
        i = 0
        while self.array[i] < e:
            i += 1 #오른쪽으로 옮겨주기

        self.size -= 1
        while i < self.size:
            self.array[i] = self.array[i+1]
            i += 1

    def __eq__(self, setB):
        if self.size != setB.size: #두 집합의 크기가 같지 않으면 비교 할 수 없음
            return False
        
        for i in range(self.size):
            if self.array[i] != setB.array[i]:
                return False
        return True
    
    def append(self, e):
        self.array[self.size] = e #비어있는 공간의 첫번째 인덱스
        self.size += 1


    def union(self, setB): #합집합
        setC = SortedArraySet()

        i = 0; j = 0 #i=setA의 인덱스, j = setB의 인덱스
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                setC.append(a)
                i += 1; j+= 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                setC.append(b)
                j += 1

        while i < self.size: #플러싱?슁?
            setC.append(self.array[i])
            i += 1

        while j < setB.size:#플러싱?슁?
            setC.append(setB.array[j])
            j += 1

        return setC

    def intersect(self, setB): #교집합
        setC = SortedArraySet()

        i = 0; j = 0
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                setC.append(a)
                i += 1; j += 1

            elif a < b: #이땐 setA의 원소가 교집합이 될 수 없다 
                i += 1

            else:
                j += 1
                  # 교집합은 플러싱 할 필요 없음
        return setC
    
    def difference(self, setB): #차집합
        setC = SortedArraySet()

        i = 0; j = 0
        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                i += 1
                j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                j += 1

        while i < self.size:
            setC.append(self.array[i])
            i += 1
            
        return setC

if __name__ == "__main__":
    import random 

    setA = SortedArraySet()
    setB = SortedArraySet()

    for i in range(5):
        setA.insert(random.randint(1,9))
        setB.insert(random.randint(1,9))
    
    print('Set A :', setA)
    print('Set B :', setB)

    e = int(input('Input to delete :'))
    setA.delete(e)
    print('SetA :', setA )

    print(setA == setB)

    print('A U B :', setA.union(setB))
    print('A n B :', setA.intersect(setB))
    print('A - B :', setA.difference(setB))