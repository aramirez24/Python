#Llista de variables
preu = float(input("Introdueix el preu del producte "))
descomptePreu = float(input("Introdueix el tant per cent "))
descompteIVA = float(input("Introdeix el tant per cent d'IVA "))

#Càlculs
descompteCalculat = (descomptePreu / 100) * preu
IVA = (descompteIVA / 100) * preu

preuDescompte = preu - descompteCalculat
preuFinal = preuDescompte + IVA

#Resultat
print(preuFinal)