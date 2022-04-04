def search(liste, toFind):
	iterations = 0
	lower = 0
	higher = len(liste)

	while True:
		mid = (lower+higher) // 2

		if liste[mid] == toFind:
			return mid, iterations
		elif liste[mid] > toFind:
			higher = mid
			mid = (lower+higher) // 2
		elif liste[mid] < toFind:
			lower = mid
			mid = (lower+higher) // 2
		iterations+=1

liste = [1, 2, 4, 8, 20, 44, 50, 67, 101, 4059, 9001, 9002]
mid, iterations = (search(liste, int(input("Skriv inn et tall programmet skal finne: "))))
print(f'Tallet er på indeks {mid}')
print(f'Koden måtte se på {iterations} verdier')