# Pràctica 3 - Endevina!

---

## Enunciat de la pràctica

Fes un programa en Python que pensi un número aleatori entre **1 i 100**.

El programa ha de:

- Preguntar repetidament el número fins que l'usuari l'endevini
- Indicar si el número és **més gran** o **més petit** en cas d'error
- Mostrar en quants intents s'ha aconseguit encertar

---

## Funcionament

1. El programa genera un número aleatori entre 1 i 100
2. L'usuari introdueix números per intentar endevinar-lo
3. El programa dona pistes:
   - "És més gran"
   - "És més petit"
4. Quan s'encerta, es mostra el nombre d'intents

---

## Exemple

(Suposant que el número és 30)


Ordinador: Quin número he pensat?
Usuari: 50
Ordinador: És més petit

Ordinador: Quin número he pensat?
Usuari: 20
Ordinador: És més gran

Ordinador: Quin número he pensat?
Usuari: 30
Ordinador: Has encertat en 3 intents

---

## Millora del programa

Implementa una segona versió amb aquestes condicions:

- El número secret està entre **1 i 10**
- L'usuari només té **3 intents**
- El joc acaba quan:
  - L'usuari encerta el número, o
  - S'esgoten els intents

### 📢 Resultat final

Al final del programa s’ha de mostrar:

- Si l’usuari **ha guanyat o perdut**
- Quin era el **número secret**
