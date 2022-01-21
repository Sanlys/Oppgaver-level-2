#HTML text tag parser

def splitter(S):
	strings = []

	start = 0
	for i, x in enumerate(S):
		if x == "<":
			start = i
			print("fant < paa plass", i)
		if x == ">":
			print("fant > paa plass", i)
			strings.append(S[start:i] + ">")

	print("Raa string",S)
	print("strings funnet:", strings)
	return strings

def parser(S):
	start = 0 						# Definerer startpunkt, dette endres av koden under
	end = 0 						# Definerer endpunkt, dette vil ogsaa endres av koden under

	# Start og endpunkt brukes til aa vise hvor den nederste loopen skal starte og slutte aa printe
	# Startpunktet blir ogsaa brukt saann at sluttpunktet ikke blir feildefinert, siden den S[i] er '<' helt paa starten av ...
	# ... en vanlig html tag, vil dette definere end som 0, som da vil skrive ut feil informasjon.

	for i, item in enumerate(S): 	# Enumerate brukes til aa faa en indeks
		if item == '>': 			# Sjekker om naaverende item er '>', som vil bety at det er slutten av den foerste taggen
			start = i + 1 			# Plusser paa 1 paa indeksen, saann at det ikke vil bli '>', men det foerste tegnet etter tegnet
			break					# Lukker ut av for loekken naar den har funnet den riktige startindeksen

	while S[start] == ' ':			# Hopper over mellomrom paa starten av en string.
		start += 1					# oeker med en, det er dette som gjoer at den kan hoppe over *alle* mellomrom

	for i in range(start, len(S)):	# Denne loekken finner slutten, den starter fra start, grunnet paa linje 8-9
		if (S[i] == '<'):			# Sjekker om verdien paa "i" i stringen S er lik '<'
			end = i 				# Setter end verdien
			break					# Lukker ut av loekken naar den har funnet sluttindeksen

	string = ""						# Setter en tom string, som kan appendes til i loekken
	for i in range(start, end):		# En loop mellom start- og sluttindeks, dette vil da bli plaintext, uten html taggene
		string += S[i]				# Appender verdien av indeksen i av strengen S til string
	print(string)					# Skriver ut stringen naar den er ferdig med aa appende.
	 
def listParser(S):
	for i in S:
		print("parsing:",i)

# Definerer bare variablene som skal brukes i parser funksjonen	 
linje1 = "<p>Her blir det brukt en P tag</p>"
linje2 = "<h1>Programmet vet ikke hva taggene betyr, men den bruker posisjonen for aa finne ut hvor teksten ligger</h1>"
linje3 = "<hei>Jeg syntes dette er et praktisk bruk av string datatypen</hei>"
linje4 = "<tag>Flere tags i samme <__>string</__>asdasd</tag>"
#Kaller parser funksjonen med variablene definert over
parser(linje1)
parser(linje2)
parser(linje3)

listParser(splitter(linje4))