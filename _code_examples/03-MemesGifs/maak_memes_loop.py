from PIL import Image, ImageFont, ImageDraw


# Laad het Impact lettertype
lettertype = ImageFont.truetype("impact.ttf", 40)

# Tekstbestand openen
file = open("meme_teksten.txt", "r")
meme_nummer = 1

# Eerste regel lezen
tekst = file.readline()

while tekst:

    tekst = tekst.replace('\\n',"\n").upper()

    # Laad de achtergrond afbeelding in de variabele: achtergrond
    achtergrond = Image.open("meme_background.jpg")

    # Afmetingen opslaan in eigen variabelen
    breedte = achtergrond.width
    hoogte = achtergrond.height
    
    # Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
    tekengebied = ImageDraw.Draw(achtergrond)

    # Bereken de breedte en hoogte van de tekst
    tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 

    # Tekst positie berekenen
    tekst_x = (breedte - tekst_breedte) / 2
    tekst_y = (hoogte - tekst_hoogte) / 2  

    # De tekst schrijven
    tekengebied.multiline_text((tekst_x, 20), tekst, font=lettertype, fill=(0,0,0), align="center")
    tekengebied.multiline_text((tekst_x-2, 18), tekst, font=lettertype, fill=(255,255,255), align="center")

    # En opslaan onder een andere naam
    bestandsnaam = "meme_met_tekst_" + str(meme_nummer) + ".jpg"
    achtergrond.save(bestandsnaam)

    # Volgende regel lezen in variabele opslaan
    tekst = file.readline()

    # Nummer met 1 ophogen
    meme_nummer = meme_nummer + 1

