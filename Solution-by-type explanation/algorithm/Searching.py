def sequentialSearch(A, key): #순차탐색
    n = len(A)
    for i in range(n):
        print(A[i], end=" ")
        if A[i] == key:
            return i
    
    return -1

def rBinarySearch(A, key, low, high): #재귀버전
    if(low > high):
        return -1
    
    mid = (low + high) // 2

    print(A[mid], end=' ')

    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return rBinarySearch(A,key, low, mid-1)
    else:
        return rBinarySearch(A,key, mid+1, high)

def iBinarySearch(A, key): #반복버전
    low = 0; high = len(A) -1
    
    while(low <= high):
        mid = (low + high) // 2
        print(A[mid], end=' ')

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid -1
        else:
            low = mid + 1

    return -1           #while을 빠져나왔을 때, mid를 못찾았을 때
    
def interpolation_search(self, key):
        low = 0
        high = self.size - 1

        while low <= high and self.array[low] <= key <= self.array[high]:
            # 보간 탐색에서의 middle 값 계산
            middle = int(low + (high - low) * (key - self.array[low]) / (self.array[high] - self.array[low]))

            if self.array[middle] == key:
                return middle
            elif self.array[middle] < key:
                low = middle + 1
            else:
                high = middle - 1

        return -1  # 찾지 못한 경우 -1 반환
    
if __name__ == "__main__":
    import random
    from Sorting import selectionSort


    a = []
    for i in range(15):
        a.append(random.randint(1,100))

    selectionSort(a)
    print('A[] =', a)
    
    key = int(input('Input Search Key : ')); print()
    
    print('Sequential Search : %d' % sequentialSearch(a,key))
    print('rBinarySearch : %d' % rBinarySearch(a,key,low=0,high=14))
    print('iBinarySearch : %d' % iBinarySearch(a,key))
    # print('iBinarySearch : %d' % interpolation_search(key))


