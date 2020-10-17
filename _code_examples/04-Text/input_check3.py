import re

while True:

    invoer = input("Voer je telefoonnummer in: ")
    patroon = '^06-?\d{8}$'
    matches = re.findall(patroon, invoer)
    
    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt nummer in juiste formaat:", matches[0])



while True:

    invoer = input("Voer je postcode in: ")
    patroon = '^[1-9][0-9]{3}\s?[A-Z]{2}$'
    matches = re.findall(patroon, invoer)
    
    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het postcode in het juiste formaat ingevoerd is.
print("Bedankt postcode in juiste formaat:", matches[0])


while True:

    invoer = input("Voer je nummerbord in: ")
    patroon = '^[A-Z]{2}-[0-9]{3}-[A-Z]{3}$'
    matches = re.findall(patroon, invoer)
    
    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het nummerbord in het juiste formaat ingevoerd is.
print("Bedankt kenteken in juiste formaat:", matches[0])

