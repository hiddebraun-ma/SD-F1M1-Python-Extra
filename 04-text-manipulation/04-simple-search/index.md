---
title: Simpele zoekmachine
---

Weet je nog hoe je bij de opdrachten over bestanden en mappen een tekstbestand hebt gemaakt en dit bestand regel voor regel hebt gelezen?

Dat ga je nu nog een keer doen. Je gaat een simpele *email scraper* maken die alle email adressen uit een tekstbestand gaat matchen met een regular expression.

---

## Tekstbestand downloaden

> [Download eerst dit tekstbestand](tekstmetemails.txt). Hierin staat een dummy (onzin) tekst met hier en daar een e-mail adres.

Zet dit tekstbestand in je map en maak daar nu een nieuw Python bestand aan met de naam `zoek_emails.py`.

> Aan jou de taak om met de kennis uit deze les om de Python code te schrijven die:
 
- Het gedownloade tekstbestand opent en regel voor regel leest.
- Een regular expression gebruikt om in elke regel ALLE email adressen in de tekst te vinden.
- Wat is de juiste regular expression voor een email adres? [Gebruik Google](){:target="_blank"} of maak hem zelf. (gebruik die regex101.com website om te testen!) 
- Deze email adressen toe te voegen aan een aparte list variabele: `emails`.
- Alle emails op het scherm tonen.

---

## De regular expression bepalen en code schrijven 

> In één van de komende Flex les gaan we dit samen coderen. Probeer eerst of je zelf uit deze puzzel komt.

Hier heb je alvast een eerste begin van de code (vul op de `...` jouw code in)

```python
import re

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()
   
    while regel:

        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"..."

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(...)

        # Alle gevonden emails aan de email list toevoegen
        ...
        
        # Volgende regel lezen
        regel = bestand.readline()

print(emails)

```

#### Tip: 
Met de `.extend()` functie van een list kun je de inhoud van de ene lijst aan de andere lijst toevoegen:

```python
emails = ["a","b","c"]
andere_lijst = [1,2,3,4]
emails.extend(andere_lijst)

print(emails)

# Uitvoer: ['a', 'b', 'c', 1, 2, 3, 4]
 
```

---

## Extra uitdagingen

Is het gelukt? Probeer dan nog deze extra uitdagingen.

#### Uitdaging 1 
Schrijf alle gevonden adressen in een apart bestand, elk op een eigen regel.\

#### Uitdaging 2 
Verander het script zodat je het als volgt op de command line kunt uitvoeren:

```python
python zoek_emails.py tekstbestand.txt
```

> Nu is het script herbruikbaar voor gebruik met andere tekstbestanden. 

> Test of het werkt met andere tekst bestanden met email adressen. 

> Maak er anders zelf een paar om te testen.

---

## Klaar! Je werk op Github zetten

Zorg er voor dat je alles wat je hebt gemaakt commit en naar Github pusht, zodat duidelijk is wat je hebt gedaan en hoe ver je bent gekomen. Hier lees je hoe je dat doet:

[Je werk *committen* en *pushen* naar Github](../../00-setup/commit_push.html){:class="next"}

> Dit was wel een flinke opdracht en best ingewikkeld. Dus neem je tijd om er aan te werken.
 
> Belangrijkste is dat je echt de tijd neemt om alle stappen te doen. Het hoeft niet meteen af, maar liefst wel binnen twee weken.

> Vraag om hulp tijdens de Flex Python Extra lessen als je vastloopt! 


