class TrieNode:
	
	def __init__(self, ch):
		self.ch = ch
		self.children = {}
		self.count = 0
		self.ew = False
		
class Trie:
	
	def __init__(self):
		self.root = TrieNode('*')
		
	def add(self, word):
		curr_node = self.root
		for ch in word:
			if ch not in curr_node.children:
				curr_node.children[ch] = TrieNode(ch)
			curr_node = curr_node.children[ch]
			curr_node.count += 1
		curr_node.ew = True
	
	def search(self, word):
		if word == "":
			return True
		
		curr_node = self.root
		for ch in word:
			if ch not in curr_node.children:
				return False
			curr_node = curr_node.children[ch]
		return curr_node.ew
		
	def is_prefix(self, word):
		if word == "":
			return True
		
		curr_node = self.root
		for ch in word:
			if ch not in curr_node.children:
				return False
			curr_node = curr_node.children[ch]
		if curr_node.count > 1:
			return True
		return False
		

words = ["aa", "ab", "ac", "ad", "a"]
cont = 0
trie = Trie()

for word in words:
	trie.add(word)
	
for word in words:
	is_ = trie.is_prefix(word)
	if not is_:
		cont += 1
	
print(str(cont))	
#print(trie.search("ab"))
#print(trie.is_prefix("a"))










	

