class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoubleLinkedList:
	def __init__ (self):
		self.head = None

	def addNode (self, data):
		nyNode = Node(data)
		nyNode.next = self.head

		if self.head != None:
			self.head.prev = nyNode
		self.head = nyNode

	def appendNode(self, data):
		nyNode = Node(data)
		nyNode.next = None
		if self.head == None:
			nyNode.prev = None
			self.head = nyNode
			return
		last = self.head
		while (last.next != None):
			last = last.next
		last.next = nyNode
		nyNode.prev = last
		return
"""
	def display(self):
		gjeldene = self.head

		if(self.head == None):
			print("List is empty")
			return
		print("Noder i linked list: ")
		while(gjeldene != None):
			print(gjeldene.data)
			gjeldene = gjeldene.next

	def displayReverse(self):
		gjeldene = self.head

		if self.head == None:
			print("List is empty")
			return
		print("Noder i linked list reversert: ")
		while gjeldene != None:
			print(gjeldene.data)
			gjeldene = gjeldene.next
"""

	def display(self):
		if self.head != None:
			print("List is empty")
			return
		else:
			n = self.head
			while n != None:
				print(n)
				n = n.next

minLinkedList = DoubleLinkedList()

inp = ""
while True:
	inp = input("X koordinat: ")
	if inp == "x" or inp == "X":
		break
	inp2 = input("Y koordinat: ")

	minLinkedList.appendNode((inp, inp2))

print("Path: ")
minLinkedList.display()
#minLinkedList.displayReverse()