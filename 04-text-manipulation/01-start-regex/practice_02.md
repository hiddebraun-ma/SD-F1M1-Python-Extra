---
title: Regular Expressions oefenen 2
---

Voor elk voorbeeld hieronder doe je het volgende :

> Voer de regular expression en de test string in op de regex101.com website en kijk wat er gematcht wordt! De matches krijgen een kleur

> Maak van elk voorbeeld een screengrab en sla hem op in je folder als bewijs!

---

## Zoeken naar meerdere letters in een tekst

Wil je alleen een paar letters matchen, zonder dat ze in een bepaalde volgorde staan dan gebruik je de *range* operator: `[<letters>]`.

Zoeken naar de *a* en de *m* doe je dan met deze regular expression: `[am]`. 

| Regular expression  | Test string               | Matches                                            |
| ------------------- | ------------------------- | -------------------------------------------------- |
| [am]                | Mediacollege Amsterdam    | Medi**a**college A**m**sterd**a****m**             |
| [eA]                | Mediacollege Amsterdam    | M**e**diacoll**e**g**e** **A**mst**e**rdam         |   

---

### Zelf proberen 
Gebruik de regex101.com website. **Maak screenshots en bewaar ze in je map!**

- Match de letters `y` en `t`, `Python is my first language, yeet!`.
- Match de letters `X` en `x` in de test string `Xerox`.
- Maak screenshots en bewaar ze in je map

---

## Zoeken naar letters in juiste volgorde (woorden)
Geef je meerdere letters op, maar NIET binnen de `[]` dan moeten ze in die volgorde staan. 

| Regular expression  | Test string               | Matches                                            |
| ------------------- | ------------------------- | -------------------------------------------------- |
| dam                 | Mediacollege Amsterdam    | Mediacollege Amster**dam**                         |
| col                 | Mediacollege Amsterdam    | Media**col**lege Amsterdam                         |

---

## Volgende stap
[Oefenen met reeksen](practice_03){:class="next"}
