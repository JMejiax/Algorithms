# We can represent a graph by using an adjacency list:

# This class are gonna construct the adjacency list, and in order to da that,
# we need the nodes and then add the edges
class Graph:
	def __init__(self, Nodes, is_directed=False):
		self.nodes = Nodes
		self.adj_list = {}
		self.visited = []
		self.is_directed = is_directed
		# Set an empty list for each node
		for node in self.nodes:
			self.adj_list[node] = []
			self.visited.append(False)
			
	# This function is gonna add an edge to an specific node
	def add_edge(self, u, v):
		self.adj_list[u].append(v) 
		# If the graph is directed means that (A, B) is not equal to (B, A)
		if not self.is_directed:
			self.adj_list[v].append(u)
	
	# This function return de count of nodes connected to a specific node
	def degree(self, node):
		return len(self.adj_list[node])
		
	# This function print the adjancecy list
	def print_adj_list(self):
		for node in self.adj_list:
			print(node, "->", self.adj_list[node])
	
	# Recursive function to visit all nodes using depth first search algo
	def dfs(self, at):
		if self.visited[at]:
			return 
		self.visited[at] = True
		print(at, "->", self.adj_list[at])
		neighbours = self.adj_list[at]
		for next in neighbours:
			self.dfs(next)

# all_edges = [("A", "B"),("A", "C"),("B", "D"),("C", "D"),("C", "E"),("D", "E")]
# nodes = ["A", "B", "C", "D", "E"]

all_edges = [(1, 2),(1, 3),(3, 4)]
nodes = [1, 2, 3, 4, 5]
graph = Graph(nodes)
# graph.print_adj_list()

for u, v in all_edges:
	graph.add_edge(u, v)

#graph.print_adj_list()

# graph.dfs(4)
r = graph.bfs(1, 3)
print(r)
