
# array of edges, directed
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# convert to adjacency matrix from edge list
M = []
for i in range(n):
    M.append([0] * n)

for t, f in A:
    M[t][f] = 1

for arr in M:
    print(arr)

# convert to adjacency list from edge list (undirected graph)
h = {}
for t, f in A:
    if t not in h:
        h[t] = []
    if f not in h:
        h[f] = []

    h[t].append(f)
    h[f].append(t)

print(h)

# convert to adjacency list from edge list
h = {}
for t, f in A:
    if t not in h:
        h[t] = []

    h[t].append(f)

print(h)

print("\nRECURSIVE DFS\n")

# recursive DFS for a graph
source = 0
seen = set()
seen.add(source)

def dfs_recursive(val):
    print(val)
    if val in h:
        for nei in h[val]:
            if nei not in seen:
                seen.add(nei)
                dfs_recursive(nei)

dfs_recursive(source)

print("\nITERATIVE DFS\n")

# iterative DFS for a graph
source = 0
seen = set()
stack = [source]
seen.add(source)

while stack:
    node = stack.pop()
    print(node)
    if node in h:
        for nei in h[node]:
            if nei not in seen:
                seen.add(nei)
                stack.append(nei) 

print("\nBFS FOR GRAPH\n")

# BFS for a graph
source = 0
seen = set()
q = [source]
seen.add(source)

while q:
    node = q.pop(0)
    print(node)
    if node in h:
        for nei in h[node]:
            if nei not in seen:
                seen.add(nei)
                q.append(nei)

# an actual class for a graph node
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f'Node({self.value})'

    def display(self):
        connects = [node.value for node in self.neighbors]
        return f'{self.value} is connected to {connects}'

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(A.display())
print(B.display())
print(C.display())
print(D.display())