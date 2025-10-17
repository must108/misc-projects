
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert(node, val):
    new = Node(val, next=node)
    return new

def find(node, val):
    temp = node
    while temp:
        if temp.val == val:
            print("Found:", val)
            return
        temp = temp.next

    print("Not found:", val)

def printList(node):
    temp = node
    while temp:
        print(temp.val, end=" ")
        temp = temp.next

    print("\n")

linked = Node(1)
linked = insert(linked, 2)
linked = insert(linked, 3)
linked = insert(linked, 4)
linked = insert(linked, 5)

printList(linked)
find(linked, 4)
find(linked, 10)

class Double:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next

head = Double(4)
tail = Double(5)
tail.prev = head
head.next = tail

def insertBeginning(head, tail, val):
    new = Double(val, next=head)
    head.prev = new
    return new, tail

def insertEnd(head, tail, val):
    new = Double(val, prev=tail)
    tail.next = new
    return head, new

head, tail = insertBeginning(head, tail, 3)
head, tail = insertBeginning(head, tail, 2)
head, tail = insertBeginning(head, tail, 1)
head, tail = insertEnd(head, tail, 6)
head, tail = insertEnd(head, tail, 7)
head, tail = insertEnd(head, tail, 8)
head, tail = insertEnd(head, tail, 9)
head, tail = insertEnd(head, tail, 10)

printList(head)
find(head, 8)
find(head, 120)
