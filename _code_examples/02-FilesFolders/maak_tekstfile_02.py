import io

# Zo open je een bestand om te overschrijven (dat is standaard in text mode)
bestand = open("test.txt", "w")

# Een tekst naar het bestand schrijven
bestand.write("Test 123!")

# Vergeet bestand niet te sluiten!
bestand.close()

# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven")
