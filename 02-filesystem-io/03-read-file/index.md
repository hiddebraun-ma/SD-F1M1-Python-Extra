---
title: Een tekstbestand lezen
---

> De instructies worden wat korter.
Je weet nu hoe je een Python bestand kunt maken en bewaren met de IDLE editor. 

*Zorg dat je in de map van deze week blijft werken, zodat alles op 1 plek staat*

## Met Python code een tekstbestand schrijven

- Maak in IDLE een nieuwe Python script met de naam: `maak_tekstfile.py`
- Importeer helemaal boven in je script de `io` module (hint: bekijk de vorige scripts)

Je kunt bestanden in een bepaalde *mode* openen: 
- r = reading (lezen)
- w = writing (overschrijven)
- a = appending (toevoegen aan einde)
- t = text mode (voor tekstbestanden, dit is standaard)
- b = binary mode (binaire mode)

Je gaat **met code** een tekst bestand maken, voeg deze code aan je Python script toe:

```python
# Zo open je een bestand om naar te schrijven 
bestand = open("test.txt", "w")

# Een tekst naar het bestand schrijven
bestand.write("Test 123!");  

# Vergeet bestand niet te sluiten!
bestand.close()
```

> Controleer of het tekstbestand is aangemaakt en dat er tekst in staat.

---

## Tekstbestand lezen in read-only mode
Nu gaan we het tekstbestand expres in **read-only** mode lezen en proberen de tekst te veranderen.
Voeg onderaan je script de volgende regels toe:

```python
# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven")
```

> Krijg je een foutmelding? Zo ja, waarom zou dat zijn? 
> Maak een screengrab en bewaar deze. 

---

## Tekstbestand lezen met read()
Je kunt een bestand in 1x helemaal inlezen en wat met de inhoud doen.
Dit kunt je doen met de `read()` functie die je op het geopende bestand kunt aanroepen.

Maak een nieuw Python bestand: `lees_bestand.py` 

```python
import io

# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
inhoud = bestand2.read()

# De inhoud op het scherm zetten:
print("De inhoud van het bestand is:")
print(inhoud)

```


### Aan de slag
[Tekstbestand regel voor regel lezen](../04-read-lines){:class="next"}


