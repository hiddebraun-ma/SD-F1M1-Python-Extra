---
title: Maken van een bot
---

Om je eigen Discord bot te maken met Python hebben we eerst een Discord Applicatie en een bot user nodig.

## Aanmaken van de Discord applicatie
Discord geeft developers de mogelijkheid om veel verschillende soorten applicaties te maken. Bots zoals jullie deze les maken, maar ook applicaties om Discord te integreren in games.

* Ga naar Discords Developer Portal https://discord.com/developers/applications
* Klik op New Application
* Geef jouw applicatie een naam. (Bijvoorbeeld MyFirstBot)
    * De naam van jouw applicatie is niet perse hetzelfde als de naam van je bot.

We hebben nu onze eerste Discord applicatie gemaakt. De volgende stap is om hier een bot van te maken.

## Bot maken

* Ga naar Bot en klik op Add Bot
* De Bot user naam en afbeelding kan je hier aanpassen. 
    * MyFirstBot is inderdaad een erg stomme naam

Heel belangrijk hier is de token. De token is straks de magische serie van getallen en cijfers die jouw Python programma gaat verbinden met de bot applicatie op discord. De bot user

## Bot toevoegen aan de server

We hebben nu een bot user aangemaakt. Deze moet je alleen nog toevoegen aan jouw server.
* Ga links naar OAuth2 en onderaan zie je een lijst met checkboxes in een veld genaamd scopes. In deze lijst kan je aangeven wat jij wilt wat je bot allemaal kan gaan doen.
* Wij willen een bot maken met basis bot functionaliteit. Klik daarom de checkbox met de label *'bot'*.
* Omdat je *bot* hebt aangevinkt is er verder onderin nu nog een veld met een lijst van checkboxes. Dit zijn alle verschillende toestemmingen die je jouw bot kan geven. Onze bot heeft er maar 2 nodig;
    * Selecteer ‘Send Messages’ zodat onze bot berichten kan maken.
    * Selecteer ook ‘Read message history’ onze jouw bot berichten kan lezen.

Boven Bot Permissions, in Scopes wordt er een URL aangemaakt. Wanneer je jouw bot de juiste permissions hebt gegeven kan je de link kopieeren en in de browser plakken. 
Hier kan je selecteren in welke server je de bot wilt hebben. Klik op Continue en Authorize om de bot toe te voegen aan jouw eigen server.

## Volgende stap
[Installeren Discord.py](../02-install-discordpy){:class="next"}