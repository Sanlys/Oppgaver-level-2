class Node:
	def __init__(self, data):
		self.leftnode = None
		self.rightnode = None
		self.value = data
class Tree:
	def __init__(self):
		self.root = None
		self.steps = 0

	def printTree(self):
		if self.root != None:
			self._printTree(self.root)

	def _printTree(self, node):
		if node != None:
			self._printTree(node.leftnode)
			print(str(node.value))
			self._printTree(node.rightnode)

	def fastPrint(self, toFind):
		self.steps += 1
		if self.root != None:
			if self.root == toFind:
				print(self.root)
				return
			self._fastPrint(self.root, toFind)

	def _fastPrint(self, node, toFind):
		self.steps += 1
		if node != None:
			if toFind == node.value:
				print(node.value)
				return
			if toFind > node.value:
				self._fastPrint(node.rightnode, toFind)
			else:
				self._fastPrint(node.leftnode, toFind)

	def add(self, data):
		if self.root == None:
			self.root = Node(data)
		else:
			self._add(data, self.root)

	def _add(self, data, node):
		if data < node.value:
			if node.leftnode != None:
				self._add (data, node.leftnode)
			else:
				node.leftnode = None(data)
		else:
			if node.rightnode != None:
				self._add(data, node.rightnode)
			else:
				node.rightnode = Node(data)

# Denne koden lar en bruker legge inn tall, ogsaa finne tall paa en rask maate.
# Dette vil bare fungere om disse tallene er sortert.

tree = Tree()

tall = 1
while tall != 0:
	tall = int(input("Legg til ett tall. > "))
	if tall != 0:
		tree.add(tall)

tall = int(input("Skriv inn tallet du vil finne. > "))

tree.printTree()
print('\n\n')
tree.steps = 0
tree.fastPrint(tall)
print("Antall steg:", tree.steps)