---
title: Bot laten posten op discord
---

Tot nu toe heb je de client verbinding laten maken met de server en heb je de client de naam van de bot en de naam van de server laten uitprinten.  Als het goed is ziet jouw code er ongeveer zo uit. 

```python
import discord
client = discord.Client()

@client.event
async def on_ready():
    guild = client.guilds[0]

    print(client.user, "has connected to discord")
    print(guild.name, "is the name of the server")

client.run("<TOKEN>")
```

Je gaat nu de bot iets laten posten in discord. Net als een mens moet de bot en client enkele dingen weten wanneer hij een bericht achter laat op Discord. De client moeten weten:

* In welke server deze iets gaat posten
* In welk channel de bot iets gaat posten
* Wat gaat de bot posten?

## De bot een bericht laten maken
De eerste stap hebben we al gedaan. De client weet in welke server(guild) deze iets moet gaan posten.

De tweede stap is het opzoeken van het channel waarin de bot gaat posten. Dit kan je op de zelfde manier doen als hoe je de guild hebt uitgekozen; je pakt de eerste channel die je tegenkomt in de lijst van channels. Voeg de volgende code toe aan de `on_ready()` functie.

> In veel gevallen wil je berichten sturen naar specifieke channel. Hier pak je de eerste die je vindt. Later gaan we kijken naar betere methodes.

```python
channel = guild.text_channels[0]
print(channel.name, "is the name of the channel")
await channel.send("I'm online!")
```

> Omdat de messages lang en kort kunnen zijn, en internet snelheden ook erg verschillen weet de Python client niet van te voren hoe lang deze bezig is met het bericht te versturen. Door `await` te gebruiken gaat de client wachten tot het bericht is verstuurt voordat de client verder gaat met de code.

Voer het script uit en kijk of je verschillende teksten kan plaatsen. Eventueel kan je ook met opmaak experimenteren. 

## Volgende stap
[Script laten reageren op berichten](../06-reageren/){:class="next"}