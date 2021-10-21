---
title: Reageren op berichten
---

Je gaat nu de bot laten reageren op berichten. Veel bestaande bots reageren op verschillende commands zoals !ban, !tempban, !clear en meer. Ook heb je veel bots waarmee je spellen kan spelen of andere leuke features.

De event handler de we gaan gebruiken is `on_message`. Deze wordt aangeroepen zodra er een bericht wordt geplaatst.

Als je deze code toevoegt aan jouw client en je jouw python script runt zul je zien dat bij alle berichten die op jouw server geplaatst worden jouw bot allerlei informatie uit 'print'.

```python
@client.event
async def on_message(message):
    print(message.channel.name, "the message was posted from this channel")
    print(message.content)
    print(message.author,"is the user who wrote the message")
    print(message.created_at,"is when the message was posted")
    print(message.channel,"is the channel this message was posted in")
```

Als je de bot wilt laten reageren op berichten, bijvoorbeeld 'Hallo' zeggen tegen mensen die iets zeggen heb je 2 dingen nodig.
* De bot moet weten wanneer iets gezegd wordt.
* De bot moet weten in welk kanaal hij iets terug moet zeggen.

Beide dingen weten we. De bot roept de `on_message` functie aan iedere keer als er iets gezegd wordt. Wanneer de functie wordt aangeroepen krijg je ook mee in welk kanaal er iets gezegd wordt.
Voeg deze regel code maar toe aan de functie:
```python
await message.channel.send("Hello " + message.author)
```

>tip: Je kan je client sluiten door op Control+C te drukken.

Je zal waarschijnlijk zien dat de bot op zichzelf gaat reageren. Dit is niet de bedoeling. 
De bot moet reageren op een gebruiker *als* de gebruiker geen bot is. Voeg hiervoor een if-statement toe aan de code.
```if message.author.bot == False:```

Voeg deze if statement toe aan de functie en plaats de ```message.channel.send``` in de if-statement.
Nu zal de bot niet meer reageren op de berichten die hij zelf plaatst!


## Klaar! Je werk op Github zetten

Zorg er voor dat je alles wat je hebt gemaakt commit en naar Github pusht, zodat duidelijk is wat je hebt gedaan en hoe ver je bent gekomen. Hier lees je hoe je dat doet.

[Je werk *committen* en *pushen* naar Github](../../00-setup/commit_push.html){:class="next"}

> Vergeet niet je token weg te halen

> Dit was wel een flinke opdracht en best ingewikkeld. Dus neem je tijd om er aan te werken.
 
> Vraag om hulp tijdens de Flex Python Extra lessen als je vastloopt! 