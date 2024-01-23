import queue 
class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def isExternal(self): #단말노드일때
        return self.left is None and self.right is None
    
def preOrder(root):
    if root:
        print('[%c]'% root.data, end='')
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        
        inOrder(root.left)
        print('[%c]'% root.data, end='')
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print('[%c]'% root.data, end='')

def levelOrder(root):
    Q = queue.Queue()
    Q.put(root) #루트노드 집어넣기
    while not Q.empty():
        root = Q.get() #꺼내기
        print('[%c] '% root.data, end='')

        if root.left: #왼쪽 자식이 존재한다면
            Q.put(root.left)
        if root.right: #오른쪽 자식이 존재한다면
            Q.put(root.right)
        
def leafCount(root):
    count = 0

    if root is not None:
        if root.isExternal():
            return 1
        else:
            count = leafCount(root.left) + leafCount(root.right)


if __name__ == "__main__":
    N4 = TreeNode('D', None, None)
    N5 = TreeNode('E', None, None)
    N6 = TreeNode('F', None, None)
    N2 = TreeNode('B', N4, N5)
    N3 = TreeNode('C', N6, None)
    N1 = TreeNode('A', N2, N3)

    print('Pre : ', end=''); preOrder(N1); print()
    print('In : ', end=''); inOrder(N1); print()
    print('Post : ', end=''); postOrder(N1); print()
    print('Level : ', end='');levelOrder(N1); print()