
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = None

    def __str__(self, val):
        return str(self.val)
        

linked = Node(1)

def insert(node, val):
    new = Node(val)
    new.next = node
    return new

def search(node, val):
    temp = node
    while temp:
        if (temp.val == val):
            print("Found: ", val)
            return
        temp = temp.next

    print("Not found")


def printAll(node):
    temp = node
    while temp:
        print(temp.val)
        temp = temp.next

def delete(node, val):
    temp = node
    while temp.next:
        if temp.next.val == val:
            temp.next = temp.next.next
        temp = temp.next
    return node

linked = insert(linked, 2)
linked = insert(linked, 3)
linked = insert(linked, 4)

printAll(linked)
search(linked, 2)
search(linked, 100)
linked = delete(linked, 2)
printAll(linked)

class Double:

    def __init__(self, val, next = None):
        self.val = val
        self.next = None

    def __str__(self, val):
        return str(self.val)

def printDouble(node, val):
    temp = node
    while temp:
        print(temp.val)
        temp = temp.next

