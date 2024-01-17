class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def getHeight(root): #높이를 구하는 메서드
    if root is None:
        return 0
    
    hLeft = getHeight(root.left) #왼쪽 서브트리의 높이
    hRight = getHeight(root.right) #오른쪽 서브트리의 높이

    if hLeft >hRight:
        return hLeft + 1
    
    else:
        return hRight + 1
    
def rotateRight(p):#시계방향회전 # p = parent, c =child 
    c = p.left
    p.left = c.left 
    c.right = p
    
    return c #루트가(parent) 바뀜

def rotateLeft(p):#반시계방향회전 # p = parent, c = child
    c = p.right
    p.right = c.right
    c.left = p
    
    return c

def getBalance(root): #균형인수를 구하는 메서드
    if root is None:
        return 0
    
    return getHeight(root.left) - getHeight(root.right)

def insert(root, key):
    if root == None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    balance = getBalance(root)

    #LL
    if balance > 1 and key < root.left.key: #왼쪽으로 서브트리가 탄생했다는 뜻 #key :1  #root.left.key: 3, 
        return rotateRight(root)
    #LR
    if balance > 1 and key > root.left.key: 
        root.left = rotateLeft(root.left)
        return rotateRight(root)
    #RR
    if balance < -1 and key > root.right.key:
        return rotateLeft(root)
    #RL
    if balance < -1 and key < root.right.key:
        root.right = rotateRight(root.right)
        return rotateLeft(root)


    return root     

def in_order(root):
    if root: #root가 null이 아니면
        in_order(root.left)
        print('%2d' % root.key, end=' ')
        in_order(root.right)

def display(root, msg):
    print(msg, end='')
    in_order(root)
    print()

if __name__ == "__main__":
    root = None #root = None 이라는 것은 전체 트리를 의미. 일단 전체 트리를 None으로 설정한 것이다    
    #keys = [7,8,9,2,1,5,3,6,4]
    keys = [5,3,1,7,10, 8, 9]

    for key in keys:
        root = insert(root,key)
        display(root, '[Insert %2d]' % key)
    
    print()