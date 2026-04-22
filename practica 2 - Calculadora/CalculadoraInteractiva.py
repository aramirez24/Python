#Llista de variables
num1 = float(input("Introdueix un numero: "))
num2 = float(input("Introdueix un altre numero: "))
operador = input("Introdueix un operador ")
resultat = 0

#Càlcul + verificació de operador
while operador != "+" and operador != "-" and operador != "*" and operador != "/" and operador != "%":
    operador = input("torna a escriure ")


if operador == "+":
    resultat = num1 + num2

elif operador == "-":
    resultat = num1 - num2

elif operador == "*":
    resultat = num1 * num2
    
elif operador == "/":
    resultat = num1 / num2

elif operador == "%":
    resultat = num1 % num2

    
#Mostrem resultat
print(resultat)