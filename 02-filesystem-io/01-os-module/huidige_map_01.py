import os

# De huidige werkmap opvragen en opslaan in de variabele: werkmap
# De letters cwd staan voor: current working directory

werkmap = os.getcwd()

# Op het scherm printen
print("De huidige map is: " + werkmap)
os.mkdir("Een nieuwe map")

mapnaam = input("Welke map wil je? ")

# Als de lengte van de mapnaam > 0 is dan maken we de map
if len(mapnaam) > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + "is gemaakt."
else:
    print("Je hebt geen naam ingevoerd")
