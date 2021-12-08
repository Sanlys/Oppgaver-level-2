kontaktliste = {}

while True:
	valg = int(input("1: Legg inn ny kontakt. 2: Vis kontakter\n>"))
	if valg == 1:
		navn = input("Navn på kontakten: ")
		tlf = input("Telefonnummer til kontakten: ")
		kontaktliste[navn] = tlf
	elif valg == 2:
		for i in kontaktliste:
			print(f'Navn: {i}, Tlf: {kontaktliste[i]}')
	else:
		print("Lukker programmet")
		break