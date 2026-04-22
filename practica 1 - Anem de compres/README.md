# Pràctica 1 - Anem de compres!

## Enunciat de la pràctica

Fes un parell de programes interactius en Python que demanin:

- El DNI del client
- El preu de l'article que ha comprat
- El tant per cent de descompte
- El tant per cent d'IVA

Amb aquestes dades ha de calcular:

- El NIF (DNI + lletra)
- El preu total

---

## Càlcul del preu final

Per calcular el preu final cal seguir els següents passos:

1. **Preu amb descompte**  
   Amb el preu inicial, calcular el descompte i restar-lo.

2. **Preu final**  
   Amb el preu amb descompte, calcular l'IVA i sumar-lo.

---

## Exemples

### Exemple 1
**Dades introduïdes:**
  12345678
  1000
  10
  21

**Resultat:**
  12345678
  1110.0

---

## Càlcul del NIF

Has de fer un programa que calculi de forma automatitzada el NIF a partir del DNI.

### Entrada:
- Un número de DNI

### Sortida:
- El NIF (DNI + lletra)

### Exemples:
  Dona'm el DNI: 12345678
  El NIF és 12345678Z
  
  Dona'm el DNI: 87654321
  El NIF és 87654321X
  
  Dona'm el DNI: 44444444
  El NIF és 44444444A

---

## Contingut del projecte

En aquest projecte trobarem dos exercicis:

- **compres.py**  
  Demana dades de compra i calcula el preu final aplicant descompte i IVA.

- **CàlculDNI.py**  
  Calcula la lletra del DNI per obtenir el NIF complet.
