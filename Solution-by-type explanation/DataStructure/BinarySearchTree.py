class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#외부함수로 만들어주자
def insert_recur(root,key):
    if root == None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert_recur(root.left, key)
    elif key > root.key:
        root.right = insert_recur(root.right, key)

    return root     

# insert_iter(root, key) 버전도 만들어보자

def max_key_node(root):
    while (root != None) and (root.right!= None):
        root = root.right

    return root 
    

def min_key_node(root):
    while (root != None) and (root.left != None):
        root = root.left

    return root

def deleteNode(root, key): #root, key(삭제할 key) ex) root = 35, key = 30
    if root == None:
        return None
    
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else: #삭제할 노드를 찾았을 때 
        if root.left == None: #왼쪽 자식이 없을 때 -> 단말노드 or 오른쪽 자식만 있는 노드 
            return root.right #오른쪽 자식
        elif root.right == None: #왼쪽자식만 있는 경우
            return root.left #왼쪽 자식
        else:
            succ = min_key_node(root.right) #succ: 후계자 #root: 삭제할 노드 #제일 작은애 찾고 오른쪽 노드 = 후계짜
            root.key = succ.key # 후계자 올리기
            root.right = deleteNode(root.right, succ.key)
    return root #재귀호출했을때 기준이 됐던 루트노드  

#중위순회
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
    keys = [35,18,7,26,3,22,30,12,26,68,99]

    for key in keys:
        root = insert_recur(root,key)
        display(root, '[Insert %2d]' % key)
    
    print()
    print('\nmax key : %d' % max_key_node(root).key) #한 번 만들어보기. 최대키 찾는 메소드 -> 만듦
    print('min key : %d' % min_key_node(root).key) #한 번 만들어보기. 최대키 찾는 메소드 -> 만듦
    
    root = deleteNode(root, 30)
    display(root, '[Delete 30] : ')
    # root = deleteNode(root, 26)
    # display(root, '[Delete 26] : ')

    # root = deleteNode(root, 18)
    # display(root, '[Delete 18] : ')
    

    