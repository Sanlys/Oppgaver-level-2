#HTML text tag parser

def parser(S):
	start = 0
	end = 0

	for i, item in enumerate(S):
		if item == '>':
			start = i + 1
			break

	while S[start] == ' ':
		start += 1

	for i in range(start, len(S)):
		if (S[i] == '<'):
			end = i
			break

	string = ""
	for i in range(start, end):
		string += S[i]
	print(string)
	 
linje1 = "<p>Her blir det brukt en P tag</p>"
linje2 = "<h1>Programmet vet ikke hva taggene betyr, men den bruker posisjonen for å finne ut hvor teksten ligger</h1>"
linje3 = "<hei>Jeg syntes dette er et praktisk bruk av string datatypen</hei>"

parser(linje1)
parser(linje2)
parser(linje3)