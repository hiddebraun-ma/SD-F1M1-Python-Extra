lachen = "Ha" * 3
print(lachen)

hard_lachen = (10 * lachen) + ("Hi" * 5)
print(hard_lachen)

tekst = "The Quick Brown Fox Jumps Over The Lazy Dog"

kleine_letters = tekst.lower()
print("De tekst in kleine letters = " + tekst)

omgekeerd = tekst[::-1]
print("De tekst achterstevoren = " + omgekeerd)

gecentreerd1 = tekst.center(80)
print(gecentreerd1)

gecentreerd2 = tekst.center(80, "#")
print(gecentreerd2)

for letter in tekst:
    print(letter)

# Nu elke letter centreren en in hoofdletters
for letter in tekst:
    center_letter = letter.upper().center(10,'-')
    print(center_letter)



# Begin lengte voor het centreren van de letters
teller = 10

# Lijst met tekens die we gebruiken om te centreren
tekens = ["-","#","+","="]

## Begin lengte voor het centreren van de letters
teller = 10

# Lijst met tekens die we gebruiken om te centreren
uitvultekens = ["-","#","+","="]

# Door alle letters gaan met de for...in loop
for letter in tekst:
    # Haal het teken op van positie 0 in de lijst (eerste teken)
    teken = uitvultekens.pop(0)

    # Stel de gecentreerde tekst samen en gebruik de variabelen teller en teken 
    center_letter = letter.upper().center(teller,teken)

    # print de gecentreerde letter
    print(center_letter)

    # De teller met 1 ophogen
    teller+=1

    # Voeg het gebruikte teken weer toe achteraan de lijst
    uitvultekens.insert(len(uitvultekens),teken)
