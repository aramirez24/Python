#LLIBRERIES
import random

#VARIABLES
numAleatori = random.randrange(1, 10)
numInput = 0
intents = 3
numIntents = 0

#LOOP
for i in range(intents):

    if numInput == numAleatori:
        continue

    numInput = int(input("introdueix un numero "))

    numIntents += 1

    if numInput > numAleatori:
        print("el numero es mes petit")
    elif numInput < numAleatori:
        print("el numero es mes gran")


if numIntents == 3:
    print("has perdut, era el", numAleatori)
else:
    print("has guanyat en", numIntents, "intents")