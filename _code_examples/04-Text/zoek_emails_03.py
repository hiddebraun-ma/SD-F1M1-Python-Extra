import re, sys


if len(sys.argv) < 2:
    print("Geen tekstbestand opgegeven")
    sys.exit()

tekstfile = sys.argv[1]

emails = []

with open(tekstfile, "r") as bestand:

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
