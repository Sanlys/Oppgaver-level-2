class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoubleLinkedList:
	def __init__ (self):
		self.head = None
		self.tail = None

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

	def display(self):
		print("Hei")
		if self.head == None:
			print("List is empty")
			return
		node = self.head
		print("Noder i linked list")
		while node != None:
			print(node.data)
			last = node
			node = node.next

	def displayReverse(self):
		print("\n")
		if self.head == None:
			print("List is empty")
			return
		node = self.head
		#Finn slutten
		print("Finner slutten..")
		while node.next != None:
			print(node.data)
			node = node.next
		print("Funnet slutten!")
		print("Siste element:", node.data)
		print("\n\n")
		print("Finner starten..")
		while node != None:
			print(node.data)
			node = node.prev
		print("Funnet starten!")

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
minLinkedList.displayReverse()