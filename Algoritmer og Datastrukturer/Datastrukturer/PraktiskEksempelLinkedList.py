class Node:
	def __init__ (self, data):
		self.data = data
		self.next = next
class SingleLinkedList:
	def __init__ (self):
		self.head = None
		self.tail = None

	def addNode(self, data):
		newNode = Node(data)

		if(self.head == None):
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode

	def display(self):
		gjeldene = self.head

		if(self.head == None):
			print("List is empty")
			return
		print("Noder i linked list: ")
		while(gjeldene != None):
			print(gjeldene.data)
			gjeldene = gjeldene.next

minLinkedList = SingleLinkedList()

#Dette kan brukes til å lage en path, f.eks. i en google-maps lik tjeneste, et spill eller en simulasjon

inp = ""
while True:
	inp = input("X koordinat: ")
	if inp == "x" or inp == "X":
		break
	inp2 = input("Y koordinat: ")

	minLinkedList.addNode((inp, inp2))

print("Path: ")
minLinkedList.display()