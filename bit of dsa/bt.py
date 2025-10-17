
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

def levelorder(node):
    q = [node]

    while q:
        a = q.pop(0)
        print(a.val, end=" ")
        if a.left: q.append(a.left)
        if a.right: q.append(a.right)


levelorder(A)
print("\n")

def search(node, val):
    if not node:
        return False

    if val == node.val:
        return True

    return search(node.left, val) or search(node.right, val)

def check_searched_val(node, val):
    if search(node, val):
        print("Found:", val)
    else:
        print("Not found:", val)

check_searched_val(A, 2)
check_searched_val(A, 15)

A2 = TreeNode(8)
B2 = TreeNode(5)
C2 = TreeNode(15)
D2 = TreeNode(3)
E2 = TreeNode(7)
F2 = TreeNode(10)
G2 = TreeNode(17)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

def search_bst(node, val):
    if not node:
        return False

    if (val == node.val):
        return True

    if val < node.val: search_bst(node.left, val)
    else: search_bst(node.right, val)

def check_searched_bst(node, val):
    if search_bst(node, val):
        print("Found:", val)
    else:
        print("Not found:", val)

check_searched_bst(A2, 8)
check_searched_bst(A2, 25)
