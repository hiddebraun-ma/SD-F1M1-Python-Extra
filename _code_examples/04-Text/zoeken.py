import re

zoekwoord = input("Waar wil je naar zoeken? ")


with open("television.txt") as filestream:
    tekst = filestream.read()
    matches = re.findall(zoekwoord, tekst)
    if len(matches):
        aantal = len(matches)
        print("'" + zoekwoord + "' is " + str(aantal) + " keer gevonden")
    else:
        print(zoekwoord + " werd niet gevonden.")
