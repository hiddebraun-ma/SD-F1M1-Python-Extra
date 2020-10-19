---
title: Regular Expressions oefenen 3
---

Voor elk voorbeeld hieronder doe je het volgende :

> Voer de regular expression en de test string in op de regex101.com website en kijk wat er gematcht wordt! De matches krijgen een kleur

> Maak van elk voorbeeld een screengrab en sla hem op in je folder als bewijs!


In de onderstaande tabellen staat aan de linkerkant elke keer de *regular expression* en aan de rechterkant de *test string* waarin gezocht wordt.

---

## Alle letters of cijfers in een bepaalde reeks matchen

Soms wil je bijvoorbeeld alle letters van a tot z (het hele alfabet) matchen, of alle cijfers van 0-9.
Je wilt als regular expression een bepaalde reeks of range karakters opgeven.

Dit kan door tussen de `[]` een reeks op te geven. 

**Bijvoorbeeld**

* `[a-z]` = Match alle **kleine** letters `a` tot `z`.
* `[A-Z]` = Match alle **hoofdletters** `A` tot `Z`.
* `[a-zA-Z]` = Match **alle** letters van `a` tot `z`, dus de hoofd- EN kleine letters.
* `[0-9]` = Match de cijfers `0` tot en met `9`.

> Probeer dit nu zelf uit op de regex101.com website:

| Regular expression  | Test string                | Matches                                              |
| ------------------- | ---------------------------- | -------------------------------------------------- |
| [a-z]               | Mediacollege Amsterdam 2020  | M**ediacollege** A**msterdam** 2020                |
| [a-zA-Z]            | Mediacollege Amsterdam 2020  | **Mediacollege** **Amsterdam** 2020                |
| [a-zA-Z0-9]         | Mediacollege Amsterdam 2020  | **Mediacollege** **Amsterdam** **2020**            |

---

## Volgende stap
In de volgende stap ga je nog wat speciale *operators* oefenen. Daarna gaan we dit (eindelijk!) in Python code toepassen.

[Verder oefenen met operators](../02-regex-operators){:class="next"}

