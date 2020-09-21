import os

# Vragen om het bestand
bestand = input("Welk bestand wil je verwijderen? ")

if len(bestand) > 0:
    # controleren of dit bestand wel bestaat met os.path.exists()
    if os.path.exists(bestand):
        # Bestand verwijderen
        os.remove(bestand)
        print("Het bestand " + bestand + " is verwijderd. Jammer dan.")
    else:
        print("Dit bestand bestaat niet, sorry.")
else:
    print("Geen invoer, script zal stoppen")
