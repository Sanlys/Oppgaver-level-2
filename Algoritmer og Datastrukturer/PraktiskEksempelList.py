#String randomizer
import random

string = "Hei dette er en lang string"	# Lager en string, som skal konverteres til list

stringList = [] 						# Lager en tom liste, den skal få en string i alle elementene, ett tegn per indeks
for item in string:						# looper over alle tengene i stringen
	stringList.append(item)				# Appender alle tegnene til stringList

print(stringList)						# Printer listen

# Koden under scrambler hele stringen i en tilfeldig rekkefølge

randomOrder = []						# Lager tom liste, dette skal bli sluttresultatet som skrives ut til bruker

for i in range(0, len(stringList)):		# Looper over lengden til alle elementene, vi vil bare ha indeks, ikke verdi så vi bruker range
	randomOrder.append(stringList.pop(random.randint(0, len(stringList)-1))) # Velger et tilfeldig tegn i den første lista, fjerner det og legger det til i den andre listen. Dette vil skrive den samme stringen igjen men alle tegnene er i tilfeldig rekkefølge

print(randomOrder)						# Skriver ut den ferdige listen