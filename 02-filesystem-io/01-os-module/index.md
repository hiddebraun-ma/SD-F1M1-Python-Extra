---
title: De os module gebruiken
---

> Maak dus alle Python bestanden in de map die je net hebt aangemaakt!

## Maak een nieuw bestand
* Open de IDLE editor en maak een nieuw Python bestand 
* Sla het bestand in de werkmap en geef het de naam: `huidige_map.py`

We gaan werken met de `os` module die in Python zit.
> Een regel die begint met een `#` is een commentaar regel,die wordt niet uitgevoerd door Python maar die gebruik je om uitleg te geven over wat de code doet

```python
import os

# De huidige werkmap opvragen en opslaan in de variabele: werkmap
# De letters cwd staan voor: current working directory

werkmap = os.getcwd()

# Op het scherm printen
print("De huidige map is: " + werkmap)

``` 

Voer het script uit met F5 (of Run > Module) 

Op mijn computer is het pad:  
`/Users/hidde/Mediacollege/2020-2021/SD-F1M1-Python-Extra/02-filesystem-io/01-os-module`

Als je op Windows werkt ziet het er ongeveer zo uit:  
`C:\Code\Flex-PythonExtra\02-filesystem-io`

## Een nieuwe map maken

Je gaat nu een nieuwe map aanmaken met Python. 
Voeg deze code toe aan je script en voer het script uit (F5)

```python```
os.mkdir("Een nieuwe map")
```

In de folder waar je script staat is nu een nieuwe map gemaakt.
Verwijder de map weer (gewoon zoals je dat normaal doet)

## De gebruiker vragen om een naam voor de map
Je kunt de input functie gebruiken om een naam te vragen en de map die naam geven:

```python
mapnaam = input("Welke map wil je? ")

# Als de lengte van de mapnaam > 0 is dan maken we de map
if len(mapnaam) > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + "is gemaakt."
else:
    print("Je hebt geen naam ingevoerd")
```
