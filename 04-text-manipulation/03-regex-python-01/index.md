---
title: Regular expressions gebruiken in Python
---

Leuk natuurlijk, als die speciale patronen, regels en karakters die je kunt gebruiken om patronen te matchen, maar wanneer gebruik je ze en hoe?

> Om regular expressions te gebruiken in Python importeer je de **re** (regular expressions) module in je script.

## Simpele invoercheck: telefoonnummer
Je gaat nu een simpele regular expression gebruiken om de invoer van een gebruiker te controleren.

De flow is als volgt:
- Vraag de gebruiker met `input()` om zijn mobiele telefoonnummer
- Deze moet in het formaat `06-XXXXXXXX` worden ingevoerd.
- Telefoonnummer moet beginnen met 06, dan misschien een streepje (hoeft niet). En dan 8 cijfers (de X-en)
- Gebruik een regular expression om te kijken of er alleen cijfers in het antwoord staan
- Anders tonen we een foutmelding

Open IDLE en maak een nieuw bestand in je map: `input_check.py`

```python
# Importeer de regular expression module
import re

phone = input("Voer telefoonnummer in (alleen cijfers): ")
```

Nu moet je eerst de juiste *regular expression* verzinnen die het patroon `06-XXXXXXXX` cijfers matcht.

Open de [regex101.com](https://regex101.com/){:target="_blank"} website en kijk of je de juiste regular expression kunt vinden die 
deze test strings / telefoonnummers matcht: `0612345678` en `06-12345678`. 

---

## Volgende stap

[Verder met het telefoonnummer](index2)


