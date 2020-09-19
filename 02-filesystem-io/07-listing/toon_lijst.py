import os

# Huidige map opslaan in variable: huidige_map
huidige_map = os.getcwd()

# De os.scandir() functie leest ALLE mappen en bestanden en zet ze in een list
# De list wordt hier opgeslagen in de variabele: alle_bestanden,
alle_bestanden = os.scandir(huidige_map)

# Met een for loop en print() kun je alles uit de list op het scherm zetten
print("Inhoudsopgave van de map: " + huidige_map)
for bestand in alle_bestanden:
    # Elke bestand is weer een apart soort waar je bijvoorbeeld de naam aan kan vragen
    print(bestand.name)
