
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

### RECURSIVE ###

def preorder(node):
    if not node:
        return None
    
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

preorder(A)
print("\n")

def inorder(node):
    if not node:
        return None

    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

inorder(A)
print("\n")

def postorder(node):
    if not node:
        return None
    
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")

postorder(A)
print("\n")

### ITERATIVE ###

def preorder_iter(node):
    st = [node]

    while st:
        a = st.pop()
        print(a.val, end=" ")
        if a.right: st.append(a.right)
        if a.left: st.append(a.left)

preorder_iter(A)
print("\n")
