
# treenode
# preorder
# inorder
# postorder
# iterative preorder
# level order
# search
# bst search

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# regular binary tree
A, B, C, D, E, F, G = [
    TreeNode(1), TreeNode(3), TreeNode(17), TreeNode(14), TreeNode(5), 
    TreeNode(2), TreeNode(15)
]

A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G

# root => left => right
def preorder(node):
    if not node:
        return None

    print(node.val, end=" ")
    if node.left: preorder(node.left)
    if node.right: preorder(node.right)

preorder(A)
print("\n")

# left => root => right
def inorder(node):
    if not node:
        return None

    if node.left: inorder(node.left)
    print(node.val, end=" ")
    if node.right: inorder(node.right)

inorder(A)
print("\n")

# left => right => root
def postorder(node):
    if not node:
        return None

    if node.left: postorder(node.left)
    if node.right: postorder(node.right)
    print(node.val, end=" ")

postorder(A)
print("\n")

# left => right => root (but iterative)
def preorder_iter(node):
    s = [node]
    
    while s:
        a = s.pop()
        print(a.val, end=" ")
        if a.right: s.append(a.right)
        if a.left: s.append(a.left)

preorder_iter(A)
print("\n")

# level order. level by level. bfs.
def bfs(node):
    q = [node]

    while q:
        a = q.pop(0)
        print(a.val, end=" ")

        if a.left: q.append(a.left)
        if a.right: q.append(a.right)

bfs(A)
print("\n")

# search. some real shit.
def search(node, val):
    if not node:
        return False

    if val == node.val:
        return True

    return search(node.left, val) or search(node.right, val)

def find_val_bt(node, val):
    if search(node, val):
        print("Found:", val)
    else:
        print("Not found:", val)

find_val_bt(A, 5)
find_val_bt(A, 18)

### BINARY SEARCH TREE

A2, B2, C2, D2, E2, F2, G2 = [
    TreeNode(8), TreeNode(5), TreeNode(15), TreeNode(3), TreeNode(7),
    TreeNode(10), TreeNode(17)
]

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

bfs(A2)
print("\n")

# optimized, given the nature of a bst
def search_bst(node, val):
    if not node:
        return False

    if val == node.val:
        return True

    if val < node.val: search_bst(node.left, val)
    else: search_bst(node.right, val)

def find_val_bst(node, val):
    if search_bst(node, val):
        print("Found:", val)
    else:
        print("Not found:", val)

find_val_bst(A2, 8)
find_val_bst(A2, 18)