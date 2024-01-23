class ArraySet:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity #array = list
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def display(self):

        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

    def contains(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False
    
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1  
                return 

    def union(self, setB):
        setC = ArraySet()

        for i in range(self.size):
            setC.insert(self.array[i])

        for i in range(setB.size):
            setC.insert(setB.array[i])

        return setC

    def intersect(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC
    
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC


if __name__ == "__main__":
    S = ArraySet()
    S.insert(10)
    S.insert(30)
    S.insert(20)
    S.insert(50)
    S.display()



    #S.display(20)
    #S.display #중복은 허용 x 

    #S.delete(30)
    #S.display()

    T = ArraySet()
    T.insert(10)
    T.insert(40)
    T.insert(50)
    T.insert(15)
    T.display()

    
    S.union(T).display()
    S.intersect(T).display()
    S.difference(T).display()    

    
