---
title: Verder met telefoonnummer
---

Is het je gelukt de juiste regular expression te vinden voor de test strings:  `0612345678` en `06-12345678`?

Er zijn verschillende antwoorden mogelijk, dit is een regular expressions die de twee test nummers matcht:

`^06-?\d+$`

Hier staat:
- Begin met 06 (dit staat dus gewoon vast)
- Dan *mag* er een `-` staan. Het vraagteken er achter zegt: mag 0 of 1 keer voorkomen.
- Dan één of meer *digits*: `\d+` tot aan het einde van de tekst (`$`).
- Wil je exact 8 digits matchen dan kun je dit zo aangeven: `\d{8}`.

---

## Verder in Python

Je gaat nu de functie `findall()` van de `re` module gebruiken om te kijken of het patroon matcht.
De `re.findall()` functie geeft je een *list* met alle *matches* voor de regular expression. Of... een lege *list* als het patroon niet gematcht kan worden in de opgegeven tekst.

> Voeg dit toe aan je script:

```python
# Vragen om telefoonnummer en opslaan in de invoer variabele
invoer = input("Voer je telefoonnummer in: ")

# Dit is de regular expression die we willen vinden
patroon = '^06-?\d{8}$'

# Hier vragen we de re module om het patroon op de invoer te matchen
matches = re.findall(patroon, invoer)

# matches bevat een list met de gevonden matches van het patroon
print(matches)

``` 

> Probeer het script uit. Als het goed is krijg je alleen een list met een match als je het telefoonnummer in de juiste vorm invoert.

---

## Doorvragen tot de invoer juist is

Je kunt nu met één regular expression het juiste patroon checken.
Maar je wilt pas verder gaan als de gebruiker het telefoonnummer op de juiste manier heeft ingevoerd.

Hiervoor schrijf je een *endless loop*. Dit is een `while True:` statement die pas stopt als het telefoonnummer juist is ingevoerd. Op dat moment gebruik je `break` om uit de *endless loop* te komen.

Vervang je script nu met de volgende code:

```python
import re

while True:

    invoer = input("Voer je telefoonnummer in: ")

    # Het klopt dat er een "r" voor de regular expression staat, zo voorkom je gedoe met speciale tekens
    patroon = r"^06-?\d{8}$"
    matches = re.findall(patroon, invoer)
    
    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt nummer in juiste formaat:", matches[0])
```

---

#### Oefening 1

Pas het script nu nog een keer aan, zodat:

- De gebruiker na het telefoonnummer ook een postcode correct moet invullen.
- Het moet in het formaat `1234 AZ` zijn 
- Waarbij 1234 natuurlijk alle cijfers kunnen zijn, en AZ alle (hoofd)letters mogen zijn. 
- De spatie tussen cijfers en letter mag er staan, maar dat hoeft niet.

Sla het nieuwe script op als `input_check2.py`

> Tip 1: Probeer eerst de regular expression uit op de regex101.com website!

> Tip 2: Gebruik de Quick reference op die website voor voorbeelden van regular expressions. 

---

#### Oefening 2

Pas het script nu nogmaals aan, zodat:

- De gebruiker ook het kenteken van zijn auto moet invullen 
- Het moet in het formaat `XX-123-XXX` zijn 
- Waarbij 123 alleen getallen mogen zijn, en XX alleen geldige (hoofd)letters. 

Sla het aangepaste script op als `input_check3.py`

---

## Volgende stap
[Simpel zoek script](../04-simple-search){:class="next"}


