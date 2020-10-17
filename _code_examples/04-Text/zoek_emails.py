import re

zoekwoord = input("Waar wil je naar zoeken? ")


with open("television.txt") as filestream:
    tekst = filestream.read()
    matches = re.findall(zoekwoord, tekst)
    if len(matches):
        vervang = ">>>" + zoekwoord.upper() + "<<<"
        vervangen_tekst = re.sub(zoekwoord, vervang, tekst)
        print(vervangen_tekst)
