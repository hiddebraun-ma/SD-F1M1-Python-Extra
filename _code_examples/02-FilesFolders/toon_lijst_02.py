import os

# Huidige map opslaan in variable: huidige_map
huidige_map = os.getcwd()

# De os.scandir() functie leest ALLE mappen en bestanden en zet ze in een list
# De list wordt hier opgeslagen in de variabele: alle_bestanden,
alle_bestanden = os.scandir(huidige_map)

# Met een for loop en print() kun je alles uit de list op het scherm zetten
print("Inhoudsopgave van de map: " + huidige_map)
for bestand in alle_bestanden:    
    if bestand.is_file():
        # Dit wordt uitgevoerd als dit een normale file is
        print(bestand.name + " (BESTAND)")
    elif bestand.is_dir():
        # Dit wordt uitgevoerd als dit een dir(ectory) is
        print(bestand.name + " (MAP)")
    else:
        # Dit wordt uitgeveord als het geen file en geen dir is
        print(bestand.name + " (ONBEKEND TYPE")
