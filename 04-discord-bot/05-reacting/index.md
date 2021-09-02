---
title: Reageren op berichten
---

Je gaat nu de bot laten reageren op berichten. Veel bots reageren op verschillende commands zoals !ban, !tempban, !clear en meer. Ook heb je veel bots waarmee je spellen kan spelen of andere leuke features.

De event handler de we gaan gebruiken is `on_message`. Deze wordt aangeroepen zodra er een bericht wordt geplaatst.

Als je deze code toevoegt aan jouw client en je jouw python script runt zul je zien dat bij alle berichten die op jouw server geplaatst worden jouw bot allerlei informatie uit 'print'.

```python
@client.event
async def on_message(message):
    print(message.channel.name, "the message was posted from this channel")
    print(message.content)
    print(message.author,"is the person who wrote the message")
    print(message.created_at,"is when the message was posted")
    print(message.channel,"is the channel this message was posted in")
```

Als je de bot wilt laten reageren op berichten, bijvoorbeeld 'Hallo' zeggen tegen mensen die iets zeggen
>tip: Je kan je client sluiten door op Control+C te drukken.
