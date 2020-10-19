import re

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()
    print(regel)
    
    while regel:

        # Regular expression voor emails
        # patroon="[\w\.-]+@[\w\.-]+"
        patroon=r"\b([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)\b"

        # Zoeken naar alle emails
        gevonden = re.findall(patroon, regel)

         # Alle gevonden emails aan de email list toevoegen
        emails.extend(gevonden)

        # Volgende regel lezen
        regel = bestand.readline()


print(emails)


# Sorteren
emails.sort()

with open("alle_emails.txt", "w") as bestand:

    for email in emails:
        bestand.write(email+ "\n")
