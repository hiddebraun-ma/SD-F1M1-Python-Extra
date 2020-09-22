# Hier importeer je de os module
import os

# Zet de variabele mapnaam eerst naar een lege tekst
mapnaam = ""

# Zet de variabele lengte_mapnaam naar 0
lengte_mapnaam = 0

# Zolang de lengte_mapnaam gelijk is aan 0, blijft het script vragen om de mapnaam
while lengte_mapnaam == 0:
    # Vraag om mapnaam en sla deze op in de variabele mapnaam
    mapnaam = input("Welke naam wil je voor de map? ")

    # Sla de lengte van de mapnaam op in de variabele lengte_mapnaam
    lengte_mapnaam = len(mapnaam)

    # Als lengte_mapnaam groter dan 0 is dan maken we de map aan
    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
        # En anders melden we dat er niets is ingevuld
        print("Je hebt geen naam ingevoerd")

# ... en anders gaat de code hier verder
print("De map " + mapnaam + " is gemaakt.")
