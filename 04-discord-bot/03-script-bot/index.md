---
title: Script uit laten voeren door bot
---

Je hebt nu alles klaar om jouw bot te laten werken:

* Een eigen discord server
* Een eigen bot toegevoegd aan deze server
* Discord.py geinstalleerd op jouw computer.

## Token opzoeken
Om straks het script te laten gebruiken door de bot hebben we de access token nodig van de bot. Deze token geeft een script toegang tot alle servers waar je de bot hebt toegevoegd. Het is daarom belangrijk om deze token geheim te houden.

* Ga naar www.discord.com/developer en log eventueel in. 
* Kijk onder **Applications** en selecteer de bot die je in stap 1 hebt aangemaakt.
* Bij het tabblad **Bot** kan je de token vinden. Onthou deze locatie want de token hebben we straks nodig. 

## Python script maken

* Maak in Visual Studio een nieuwe Python file aan met de naam: `discord_bot.py`.
* Importeer *discord.py*: `import discord`
* Maak de 'client' aan. Dit is het object welke gaat communiceren met de Discord server. Je kan via dit object bij de discord API komen. Dat betekent dat je bij allemaal functies en andere objecten komen die te maken hebben met Discord. `client = discord.Client()`
* Hier ga je gebruik maken van de Token. Laat de Client verbinding maken met Discord: `client.run("<TOKEN>")`. Gebruik hier jouw eigen token in plaats van `<TOKEN>`
* Sla dit bestand op.

Je hebt nu een script gekoppeld aan de bot met deze enkele regels!

## Eerste Event Handler
We gaan beginnen met het schrijven van onze eerste Event Handler. Een event handler is zoals de naam al zegt, iets wat een event (gebeurtenis) af handelt. Er zijn een heleboel events en deze zijn (**niet** heel erg goed) beschreven in de documentatie van discord.py.

* on_ready
* on_error
* on_disconnect
* on_message
* on_message_delete
* on_message_edit
* on_reaction_add
* on_member_join


