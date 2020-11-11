# https://www.hackerrank.com/challenges/bfsshortreach/problem

def solve(nodes, edges, s):
    from collections import deque
    
    g = {}
    for i in range(1, n+1):
        g[i] = []
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)
        
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
    

eds = set()
q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    for x in range(m):
        u, v = map(int, input().split())
        eds.add((u,v))
    s = int(input())
    r = solve(n, eds, s)
    rr = []
    for i in range(1, n+1):
        if i != s:
            rr.append(r[i])
    eds = set()
    print(*rr)

