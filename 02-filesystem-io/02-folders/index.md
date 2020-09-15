---
title: Een nieuwe map maken
---

Je gaat nu een nieuwe map aanmaken met Python. 
Voeg deze code toe aan het script wat nu hebt en voer het script uit (F5):

```python
# Een nieuwe map maken met os.mkdir()
os.mkdir("Een nieuwe map")
```

> In de folder waar je script staat is nu een nieuwe map gemaakt.

![](new-folder.png)

> Probeer nu zelf een paar mappen aan te maken met de `os.mkdir()` functie.

Verwijder daarna mappen weer (gewoon zoals je dat normaal ook doet)

---

## De gebruiker vragen om een naam voor de map
- Je kunt de `input()` functie gebruiken om een naam te vragen aan de gebruiker van het programma.
- Dit sla je op in de variabele `mapnaam`. De variabele gebruik je in de `os.mkdir()` functie.
- Ook check je eerst met een `if` of er wel iets is ingevoerd.

Voeg deze code toe aan je script:

```python
# Gebruiker om de naam van de map vragen
mapnaam = input("Welke naam wil je voor de map? ")

# Als de lengte van de mapnaam > 0 is dan maken we de map
if len(mapnaam) > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + " is gemaakt.")
else:
    print("Je hebt geen naam ingevoerd")
```

> Voer het script uit. Wat gebeurt er? Maak een screenshot van de code en de bestanden.

---

## Het script beter laten werken
Als je niets invult stop het script nu. Om dat te voorkomen kun je een `while` loop gebruiken.
Deze herhaalt code zo lang een bepaalde check (condition) *wel* of juist *niet* waar is.

Je wilt dat het programma blijft vragen om een mapnaam totdat de gebruiker iets invult:

```python
# Zet mapnaam naar een lege tekst
mapnaam = ""

# Zolang de mapnaam leeg is, blijft het script vragen om de mapnaam
while len(mapnaam) === 0:
    mapnaam = input("Welke naam wil je voor de map? ")
    
    # Als de lengte van de mapnaam > 0 is dan maken we de map
    if len(mapnaam) > 0:
        os.mkdir(mapnaam)
        print("De map " + mapnaam + " is gemaakt.")
    else:
        print("Je hebt geen naam ingevoerd")

    # Als hier de mapnaam nog leeg is, wordt de while loop opnieuw uitgevoerd

# ... en anders gaat de code hier verder
```

## De nieuwe map instellen als de werkmap
In de nieuwe map gaan we nu spelen met code. We willen dus dat het script de nieuwe map als *working directory* instelt.
Dit kan met de `os.chdir()` functie.

Voeg toe onderaan het script (dus waar de map als het goed is is aangemaakt)

```python
# Verander de werkmap naar de nieuwe map
os.chdir(mapnaam))
print("De nieuwe working directory is nu: " + os.getcwd())
```

Dit betekent dat alle filesystem commando's die je nu doet worden uitgevoerd van uit die map.

> Test het maar eens: maak nog een nieuwe map aan.
> Controleer of de map op de goede plek is aangemaakt. 
  
