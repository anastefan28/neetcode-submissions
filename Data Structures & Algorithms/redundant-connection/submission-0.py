class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
    
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            self.rank[root_a] += self.rank[root_b]
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += self.rank[root_a]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for a, b in edges:
            if not dsu.union(a, b):
                return [a,b]