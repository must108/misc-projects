class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False
    
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.rank[pa] += self.rank[pb]
        return True
    
d = DSU(10)
print(d.find(1))
print(d.find(5))
print(d.union(1, 5))
print(d.find(5))
print(d.union(5, 7))
print(d.find(7))
print(d.parent)

d.union(2, 4)
d.union(4, 3)
d.union(3, 9)
print(d.parent)