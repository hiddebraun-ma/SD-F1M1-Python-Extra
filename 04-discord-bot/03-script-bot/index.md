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

## Client script maken

* Maak in Visual Studio een nieuwe Python file aan met de naam: `discord_bot.py`.
* Importeer *discord.py*: `import discord`
* Maak de 'client' aan. Dit is het object welke gaat communiceren met de Discord server. Je kan via dit object bij de discord API komen. Dat betekent dat je bij allemaal functies en andere objecten komen die te maken hebben met Discord. `client = discord.Client()`
* Hier ga je gebruik maken van de Token. Laat de Client verbinding maken met Discord: `client.run("<TOKEN>")`. Gebruik hier jouw eigen token in plaats van `<TOKEN>`.   
Deze regel code moet pas uitgevoerd worden aan het einde van de code.
* Sla dit bestand op.

Je hebt nu een script gekoppeld aan de bot met deze enkele regels! Het Python script wat we nu uitvoeren noemen we ook wel de client. We maken hier een client aan en zeggen dat de client moet gaan werken.

Dit script kan je uitvoeren door de terminal te openen in de juiste folder (kan via CMD of in Visual Studio) en type `python discord_bot.py`. Je zal zien dat er helemaal niks gebeurt. Er lijkt tenminste niks te gebeuren want jouw script maakt verbinding met jouw discord bot. Alleen je zegt *nog* niet dat de bot dan iets moet uitprinten wanneer hij verbinding heeft. Je kan het script laten stoppen door op **Control+C** te drukken.

## Event Handlers.
Om jouw bot iets te laten doen moet je weten **wanneer** hij iets gaat doen.  Een event handler is zoals de naam al zegt, iets wat een event (gebeurtenis) af handelt. Er zijn een heleboel events en deze zijn (**niet** heel erg goed) beschreven in de documentatie van discord.py.

De meest voorzelfsprekende zijn de volgende:

* **`on_ready`**    
Wordt gebruikt wanneer het de client en bot helemaal klaar zijn en alles is ingeladen.
* **`on_error`**   
 Wordt gebruikt wanneer er iets fout gaat bij de client of discord. Informatie over de error wordt meegegeven.
* **`on_disconnect`**    
 Wordt gebruikt wanneer de verbinding van de client wordt verbroken. Bijvoorbeeld wanneer het internet wordt verbroken of wanneer je de client afsluit.
* **`on_message`**     
Wordt gebruikt wanneer er iemand een bericht achter laat. Informatie over wie welk bericht waar achterlaat kan je in deze event handler gebruiken.
* **` on_member_join`**    
Wordt gebruikt wanneer er een nieuwe member in de Guild/Server komt.

## Eerste event handler
De eerste event handler die we gaan gebruiken is `on_ready`. Deze wordt aangeroepen wanneer de client helemaal gereed is en alles functioneel is. Als er dus iets nog niet helemaal goed is zal de functie niks doen.

Zet deze functie code boven `client.run("<TOKEN>")`

> Dit is niet de beste of mooiste methode van het vinden van een guild want we pakken gewoon de eerste guild/server die we kunnen vinden. Later gaan we kijken naar betere methodes.

```python
@client.event
async def on_ready():
    # De bot kan op veel verschillende servers draaien. Met deze regel code pak je de eerste server die deze bot heeft. Als jouw bot maar 1 server heeft is het makkelijk.
    guild = client.guilds[0]
    # De naam van de server printen we gelijk uit.
    print(guild.name, "is the name of the server")

    # We printen de naam van de bot user uit.
    print(client.user, "has connected to the client")
```

Voer je script uit en bewonder het resultaat!

Je hebt nu je eigen bot gemaakt en een script verbinding laten maken met de bot. Je hebt zelfs al informatie van de bot uitgelezen. In de volgende pagina ga je de bot berichten laten plaatsen.