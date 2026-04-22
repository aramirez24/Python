#llista de variables
dni = int(input("Introdueix el dni "))
llista = str("TRWAGMYFPDXBNJZSQVHLCKE")

#càlcul
residu = (dni % 23)

#resultat
print(str(dni) + str(llista[residu]))



