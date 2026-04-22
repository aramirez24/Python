#Variables
noms = []
preus = []
nom = None
preu = None

#Bucle demanar productes i preu
while nom != "$":
    nom = input("Nom del producte: ")
    if nom != "$":
        preu = float(input("Introdueix el preu: "))
        noms.append(nom)
        preus.append(preu)


#Fa print de la llibreria completa
print("---------------------")

for i in range(len(noms)):
    print(i + 1, "-", noms[i], preus[i], "€")

print("---------------------")


#Variables
total = 0
opcio = None

#Bucle comprar
while opcio != 0:
    opcio = int(input("Quin article vols comprar? posa 0 per pagar "))
    if opcio != 0:
        if opcio <= len(noms):
            total += preus[opcio - 1]
            print("Has afegit", noms[opcio - 1])
    

#Print final
print("Gràcies, el total és", total, "€")