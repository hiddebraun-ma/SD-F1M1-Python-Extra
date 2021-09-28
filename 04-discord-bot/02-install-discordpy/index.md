---
title: Installeren van discord.py
---

We hebben nu onze eigen bot gemaakt en deze toegevoegd aan de server. Maar we vertellen nog helemaal niet wat de bot moet doen.

Om de bot dingen uit te laten voeren gaan we een script aan de bot toevoegen. Om de bot het script uit te laten voeren en berichten te kunnen lezen en te plaatsen hebben we **Discord.py** nodig.

Dit is een Python *module* (een soort Python plugin) net als PIL in de vorige opdracht. Deze zit niet standaard in Python, maar die je kunt installeren met [pip](https://realpython.com/what-is-pip/){:target=_"blank"}. Pip is tegelijk met Python geïnstalleerd. 

```bash
pip install -U discord.py
```

> Mac gebruikers: gebruik dus `pip3` in plaats van `pip`

## De geinstalleerde packages bekijken
Voer nu `pip list` uit om te kijken welke *packages* je hebt geïnstalleerd.

> Als het goed is, staat *discord.py* er tussen. Anders is het nog niet geïnstalleerd. 

---

## Volgende stap
[Script bot](../03-script-bot/){:class="next"}

