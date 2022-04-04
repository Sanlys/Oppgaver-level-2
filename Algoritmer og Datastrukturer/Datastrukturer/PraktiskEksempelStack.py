stack = ["wow", "stack", "1", "2", "haha"]

stack.append("Tekst")
stack.append("Mer tekst")
stack.append("Enda mer tekst")

print(stack)

stack.pop()
stack.pop()

print(stack)

def printStack(stack):
	for i in stack:
		print(i)

#bruk av stack

stack = []
valg = 5
while int(valg) != 0:
	valg = input("0: Lukk programmet\n1: Legg til i stack\n2: Fjern fra stack og skriv ut verdi\n3: Skriv ut stack\n")
	if int(valg) == 1:
		txt = input('Input til stack: ')
		stack.append(txt)
	if int(valg) == 2:
		print(stack.pop())
	if int(valg) == 3:
		printStack(stack)
