---
title: Veel gebruikte tekst functions
---

Een string bestaat uit één of meer alfanumerieke tekens.
Deze kun je opslaan in een variabele:

```python
naam = 'Terry Gilliam'

# Dit toon de tekst in uppercase: "TERRY GILLIAM"
print(naam.upper())
```
 
Je kunt ook **direct** een string function aanroepen op de tekst zelf:  
`'Terry Gilliam.upper()`

```python
print('Terry Gilliam'.upper())
# Dit toon de tekst in uppercase: "TERRY GILLIAM"

```
 
Er zijn veel string functions die je kunt gebruiken. In de volgende oefeningen ga je er een paar uitproberen.

## Bestand maken om in te werken
Maak in IDLE een nieuw Python bestand en sla het bestand op met de naam: `text_functions.py`.

* Je gaat elke keer één *string* function uitproberen.
* Eerst krijg je een voorbeeld
* Vervolgens schrijf je zelf een eigen stukje code met die function 
* Je schrijft alle code onder elkaar in het Python bestand
* Zorg dat de code geen errors heeft. Dus elke keer uitvoeren met Run > Module (F5)

### Strings samenvoegen of herhalen
Je kunt een string herhalen met de multiplication operator: `*`

```python
lachen = "Ha" * 3
print(lachen)

hard_lachen = (10 * lachen) + ("Hi" * 5)
print(hard_lachen) 
```
 

### Een string in kleine letters zetten
Met de `lower()` function zet je een tekst(variabele) om in kleine letters.
 
```python
tekst = "The Quick Brown Fox Jumps Over The Lazy Dog"
kleine_letters = tekst.lower()
print("De tekst in kleine letters = " + tekst)

# Maak zelf een tekst variabele, zet hem om in kleine letters en print het resultaat
```

### Een string in omgekeerde volgorde zetten
Met een handige **string slicing** truc kun je dit doen.
 
```python
omgekeerd = tekst[::-1]
print("De tekst achterstevoren = " + omgekeerd)

# Maak zelf een tekst variabele, en draai hem om met deze truc
```

### Een string centreren en uitvullen met letter of symbool
Met de `center()` function kun je een tekst vergroten tot een grotere lengte en de letters die links en rechts staan opvullen met een letter die jij wilt.
 
```python
gecentreerd1 = tekst.center(80)
print(gecentreerd1)

gecentreerd2 = tekst.center(80, "#")
print(gecentreerd2)

# Zet je naam gecentreerd op het scherm met links en rechts een zelfgekozen uitvulteken
```

### Een tekst letter voor letter opvragen
Een tekst is net als een *list* ook een *sequence* van karakters. Je kunt een **for ... in** loop gebruiken om alle afzonderlijke karakters af te lopen en er iets mee te doen.

```python
for letter in tekst:
    print(letter)

# Nu elke letter centreren en in hoofdletters
for letter in tekst:
    print(letter.upper().center(10,'-')

# Maak nu zelf een eigen tekst en doe iets met elke letter in de tekst 
```

### Gewoon omdat het leuk is
Hier worden een list met separators, een loop en een oplopende teller variabele gecombineerd.

```python
# Begin lengte voor het centreren van de letters
teller = 10

# Lijst met tekens die we gebruiken om te centreren
uitvultekens = ["-","#","+","="]

# Door alle letters gaan met de for...in loop
for letter in tekst:
    # Haal het teken op van positie 0 in de lijst (eerste teken)
    teken = uitvultekens.pop(0)

    # Stel de gecentreerde tekst samen en gebruik de variabelen teller en teken 
    center_letter = letter.upper().center(teller,teken)

    # print de gecentreerde letter
    print(center_letter)

    # De teller met 1 ophogen
    teller+=1

    # Voeg het gebruikte teken weer toe achteraan de lijst
    uitvultekens.insert(len(uitvultekens),teken)
```

> Probeer te begrijpen wat deze code regel voor regel doet. 

---

## Volgende stap
Zoeken in een tekst


