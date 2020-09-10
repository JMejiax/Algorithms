class Graph:
	def __init__(self, Nodes, is_directed=False):
		self.nodes = Nodes
		self.adj_list = {}
		# self.visited = [False]*100
		self.visited = []
		self.is_directed = is_directed
		self.steps = 0
		# Set an empty list for each node
		for node in self.nodes:
			self.adj_list[node] = []
			
	# This function add an edge to an specific node
	def add_edge(self, u, v):
		self.adj_list[u].append(v) 
		# If the graph is directed means that (A, B) is not equal to (B, A)
		if not self.is_directed:
			self.adj_list[v].append(u)
			
			
	# Recursive function to visit all nodes
	def dfs(self, at):
		current = self.adj_list[at]
		if at in self.visited:
			return 
			
		if not current:
			return
		
		self.steps += 1
		self.visited.append(at)	
		for next in current:
			self.dfs(next)
		self.steps += 1

t = int(input())
start_position = 0
edges = []
nodes = []
result = []
for i in range(t):
	start_position = int(input())
	v,a = map(int, input().split()) 
	for i in range(0, a):
		edges.append(list(map(int, input().split())))
	for i in range(v):
		nodes.append(i)

	graph = Graph(nodes)

	for u,v in edges:
		graph.add_edge(u,v)
	
	graph.dfs(start_position)
	result.append(graph.steps-2)
	graph.steps = 0
	graph.visited = []
	edges = []
	nodes = []
	

print(*result, sep="\n")
"""
------------
0 -> [4, 1]
1 -> [0, 2]
2 -> [3, 6, 1]
3 -> [2]
4 -> [0, 8]
5 -> [6]
6 -> [2, 5]
7 -> [11]
8 -> [9, 12, 4]
9 -> [8, 10]
10 -> [9, 14, 11]
11 -> [10, 7]
12 -> [8, 13]
13 -> [12]
14 -> [15, 10]
15 -> [14]

1.  0  -> 4
2.  4  -> 8
3.  8  -> 9
4.  9  -> 10
5.	10 -> 14
6.  14 -> 15
7.  14 -> 15
8.  15 -> 14
9.  14 -> 10
10. 10 -> 11
11. 11 -> 7
12. 7  -> 11
13. 11 -> 10
14. 10 -> 9
15. 9  -> 8
16. 8  -> 12 
17. 12 -> 13
18. 13 -> 12
19. 12 -> 8
20. 8  -> 4
21. 4  -> 0
22. 0  -> 1
23. 1  -> 2
24. 2  -> 3
25. 3  -> 2
26. 2  -> 6
27. 6  -> 5
28. 5  -> 6
29. 6  -> 2
30. 2  -> 1
31. 1  -> 0
------------

------------
0 -> []
1 -> [2, 4, 4]
2 -> [1]
3 -> [4]
4 -> [1, 7, 1, 3]
5 -> []
6 -> []
7 -> [4, 8]
8 -> [7]

1.  1 -> 2
2.	2 -> 1	
3.	1 -> 4
4.	4 -> 7
5.  7 -> 8
6.  8 -> 7
7.  7 -> 4
8.  4 -> 3
9.  3 -> 4
10. 4 -> 1
------------

------------
"""

