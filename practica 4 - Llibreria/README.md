# Pràctica 4 - Llibreria!

## Enunciat de la pràctica

Crea un programa en Python que simuli una **llibreria escolar**.

---

## Entrada de productes

El programa ha de demanar de forma continuada:

- El **nom del producte**
- El **preu**

### Exemple:
Llapis ........ 1.2€
Bolígraf ...... 3€
Quadern ...... 2.5€
Carpeta ...... 4.2€
Goma ......... 0.4€


### Condicions per acabar la introducció:

Es pot fer de dues maneres:

- Introduir un **nombre mínim de productes (mínim 8)**  
**o bé**
- Finalitzar quan:
  - S’introdueixi un valor especial (ex: `$`)
  - El preu sigui **invàlid** (0 o negatiu)

---

## Catàleg de la llibreria

Un cop introduïts els productes, es mostrarà el catàleg:


LLIBRERIA ESCOLAR

1 - Llapis ........... 1.2€
2 - Bolígraf ......... 3.0€
3 - Quadern .......... 2.5€
4 - Carpeta .......... 4.2€
5 - Goma ............. 0.4€

0 - PAGAR


---

## Procés de compra

Després de mostrar el catàleg, el programa ha de:

- Preguntar repetidament: **"Quin article vols comprar?"**
- L’usuari tria una opció (número)
- Afegir el producte seleccionat al total

### 🧾 Finalització:

- Quan l’usuari introdueix **0 (PAGAR)**:
  - El programa surt del bucle
  - Mostra el **total a pagar**
