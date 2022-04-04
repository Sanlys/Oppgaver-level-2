queue = ['hei', 'hoi', 'hai', 'hui', 'hyi']

queue.append('halla')
queue.append('hade')
queue.append('paa')
queue.append('badet')

print(queue)

queue.pop(0)
queue.pop(0)

print(queue)

def printQueue(queue):
	for i in queue:
		print(i)

printQueue(queue)

queue = []
valg = 5
while int(valg) != 0:
	valg = input("0: Lukk programmet\n1: Legg til i queue\n2: Fjern fra queue og skriv ut verdi\n3: Skriv ut stack\n")
	if int(valg) == 1:
		queue.append(input("Skriv inn verdi: "))
	if int(valg) == 2:
		print(queue.pop(0))
	if int(valg) == 3:
		printQueue(queue)