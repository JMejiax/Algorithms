# https://www.hackerrank.com/challenges/bfsshortreach/problem

class Graph:
    def __init__(self, nodes, is_directed=False):
        self.nodes = nodes
        self.adj_list = {}
        self.is_directed = is_directed
        
        # Set nodes to the adjency list
        for node in self.nodes:
            self.adj_list[node] = []
            
    def add(self, u, v):
        self.adj_list[u].append(v)
        
        if not self.is_directed:
            self.adj_list[v].append(u)
    
    def bfs(self, s):
        prev = self.solve(s)
        return prev
    
    def solve(self, s):
        from collections import deque
        
        g = self.adj_list
        n = len(g)
        
        q = deque()
        q.append(s)
        
        dist = [-1]*(n+1)
        dist[s] = 0
        
        while q:
            node = q.popleft()
            nbs = g[node]
            for nb in nbs:
                if dist[nb] == -1:
                    dist[nb] = dist[node] + 6
                    q.append(nb)
        return dist
        



q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    graph = Graph([i for i in range(1, n+1)])
    for x in range(m):
        u, v = map(int, input().split())
        graph.add(u, v)
    s = int(input())
    r = graph.bfs(s)
    rr = []
    for e in range(1, n+1):
        if e != s:
            rr.append(r[e])
    print(*rr)

"""
21
10 6
3 1
10 1
10 1
3 1
1 8
5 2
3
6 -1 -1 -1 -1 -1 12 -1 12
"""
"""
2         
4 2
1 2
1 3
1
3 1
2 3
2
6 6 -1
-1 6
"""
"""
1
5 3
1 2
1 3
3 4
1
6 6 12 -1
"""


		
