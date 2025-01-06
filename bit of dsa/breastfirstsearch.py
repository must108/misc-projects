from collections import defaultdict

l = [[0, 1], [0, 2], [0, 3], 
     [1, 4], [1, 5], [1, 6], [1, 7],
     [2, 4], [2, 5], [2, 6], [2, 7], [2, 3]]

graph = defaultdict(list)
ret = []

for u, v in l:
    graph[u].append(v)

def bfs(graph, node):
    v = []
    q = []

    v.append(node)
    q.append(node)

    while q:
        s = q.pop(0)
        print(s, end = " ")

        for n in graph[s]:
            if n not in v:
                v.append(n)
                q.append(n)

bfs(graph, 0)

