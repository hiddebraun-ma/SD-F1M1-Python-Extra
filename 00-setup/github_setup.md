### Github repository voor Python Extra maken

Voor de Python Extra lessen werk je als volgt:

1. Je maakt éénmalig een map **Flex-PythonExtra** aan op een handige plek op jouw computer. *Onthoud die plek!*
2. Je maakt ook een Github repository aan met dezelfde naam: **Flex-PythonExtra**
3. De map **Flex-PythonExtra** op je computer koppel je vervolgens aan je **Flex-PythonExtra** Github repository 
4. Tijdens de Python Extra lessen werk je dus **ALTIJD** in de **PythonExtra** map!
5. Je maakt aan het begin van elke les een nieuwe submap aan de les van die week, met als naam het onderwerp van die week.
5. In die map zet je dus al je Python code en andere bestanden.
6. Aan het einde van de les  **commit** je alles en **push** je dit naar je Github repository. 

Hier staat hoe je die Github repository aanmaakt en koppelt aan de map. En een voorbeeld hoe je code er in zet, commit en pusht.

*Dit ga je veel doen de komende tijd!*

---

#### 1. Map maken: Flex-PythonExtra

* Ga naar de plek waar je de map wil en maak daar de map "Flex-PythonExtra"

---

#### 2. Github repository maken
Login op Github en klik op "New repository"
![](new_repository.png)

Vul de gegevens als volgt in, met jouw naam en klas en selecteer  de optie om een README.me bestand te maken. Klik dan op "Create repository":
![](create_repo.png)

---

#### 3. Github repository maken
Ga naar de map **Flex-PythonExtra** en open daar een powershell (Windows) of terminal venster (Mac)

Initialiseer een nieuwe Git repository met het volgende commando:

```bash
git init
```
![](git_init.gif)

---

#### 4. Kopieer de URL van je Github repository
Ga naar je Github repository en kopieer de **HTTPS** url onder de Code knop:
![](github_copy_url.gif)

---

#### 5. Github repository koppelen aan de Git repository op je computer

Met het commando `git remote add origin <URL>` koppel je je Github repository aan de map op je computer. Bij `<URL>` plak je de url die je in stap 4 hebt gekopieerd.
![](git_remote_add.gif)

Je kunt controleren of het gelukt is met het commando: 

```bash
git remote -v
``` 

Dit laat zien welke externe Git repository (Github) aan je lokale repository (op je computer) is gekoppeld.

---

#### 6. De laatste wijzigingen van Github halen
Nu de map goed is gekoppeld kun je alle wijzigingen die je nog niet hebt, ophalen van Github. Want (weet je nog) je hebt een README.md bestand gemaakt.

Voer nu dit commando uit:

```bash
git pull origin master
```
![](git_pull_origin_master.gif)

Hiermee haal je de `master` branch op naar je computer (de `master` is de standaard branch in Git)

**Als het goed is heb je nu het README.md bestand op je computer staan**

---

#### 7. README bestand wijzigen
Je gaat nu een wijziging doen aan het README.md bestand.  
Open het bestand `README.md` in kladblok, of een andere tekst editor en zet jouw naam en klas er in en bewaar het bestand.
![](readme_edit.gif)

---

#### 8. De wijzigingen opsturen naar Github
Nu kun je jouw wijzigingen **committen** en **pushen** naar Github. 

1. Eerst kijk je met `git status` wat de wijzigingen zijn. 
2. Dan selecteer je alle wijzigingen met `git add .`
3. Nu commit je alles met een duidelijke commit message: `git commit -m "README gewijzigd"`
4. En dan kun je de master branch naar Github (de origin) pushen  met: `git push -u origin master`

![](git_commit_push.gif)

Kijk nu in je Github repository of je commit en wijziging er staat:
![](check_commit.gif)












