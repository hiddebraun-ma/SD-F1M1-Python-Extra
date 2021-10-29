---
title: Discord bot script pushen naar Github
---

Push de bot naar github toe.

```bash
git add .
git commit -m "Mijn eerste discord bot!"
git push
```

Zodra je pusht krijg je ineens een notificatie op discord en een email!
Blijkbaar is jouw bot token 'gecompromised'. De token van van jouw bot is een extreem persoonlijk iets wat je niet mag delen, en blijkbaar heeft **iemand** die van jouw op het internet gezet.
Bots kunnen in heel veel verschillende discords draaien met verschillende niveaus van rechten. Als iemand de token zou hebben van een discord bot kunnen zij hun eigen script eraan hangen en gebruik maken van de admin rechten.

> Wanneer je jouw discord bot script gaat commmitten en pushen naar github, vergeet dan niet de token weg te halen.

Developers van grote bots slaan hun token vaak op in een extern bestand en pushen deze niet naar github. Voor nu kan je het beste de token tijdelijk uit de code halen.

In de volgende pagina ga je de bot berichten laten plaatsen.

## Volgende stap
[Script bot](../05-messaging/){:class="next"}