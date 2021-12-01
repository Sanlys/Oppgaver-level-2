#HTML text tag parser

def parser(S):
	start = 0 						# Definerer startpunkt, dette endres av koden under
	end = 0 						# Definerer endpunkt, dette vil også endres av koden under

	# Start og endpunkt brukes til å vise hvor den nederste loopen skal starte og slutte å printe
	# Startpunktet blir også brukt sånn at sluttpunktet ikke blir feildefinert, siden den S[i] er '<' helt på starten av ...
	# ... en vanlig html tag, vil dette definere end som 0, som da vil skrive ut feil informasjon.

	for i, item in enumerate(S): 	# Enumerate brukes til å få en indeks
		if item == '>': 			# Sjekker om nåverende item er '>', som vil bety at det er slutten av den første taggen
			start = i + 1 			# Plusser på 1 på indeksen, sånn at det ikke vil bli '>', men det første tegnet etter tegnet
			break					# Lukker ut av for løkken når den har funnet den riktige startindeksen

	while S[start] == ' ':			# Hopper over mellomrom på starten av en string.
		start += 1					# Øker med en, det er dette som gjør at den kan hoppe over *alle* mellomrom

	for i in range(start, len(S)):	# Denne løkken finner slutten, den starter fra start, grunnet på linje 8-9
		if (S[i] == '<'):			# Sjekker om verdien på "i" i stringen S er lik '<'
			end = i 				# Setter end verdien
			break					# Lukker ut av løkken når den har funnet sluttindeksen

	string = ""						# Setter en tom string, som kan appendes til i løkken
	for i in range(start, end):		# En loop mellom start- og sluttindeks, dette vil da bli plaintext, uten html taggene
		string += S[i]				# Appender verdien av indeksen i av strengen S til string
	print(string)					# Skriver ut stringen når den er ferdig med å appende.
	 
# Definerer bare variablene som skal brukes i parser funksjonen	 
linje1 = "<p>Her blir det brukt en P tag</p>"
linje2 = "<h1>Programmet vet ikke hva taggene betyr, men den bruker posisjonen for å finne ut hvor teksten ligger</h1>"
linje3 = "<hei>Jeg syntes dette er et praktisk bruk av string datatypen</hei>"

#Kaller parser funksjonen med variablene definert over
parser(linje1)
parser(linje2)
parser(linje3)