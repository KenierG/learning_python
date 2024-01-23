'''
Script description:
Cree una función que genere el lanzamiento de dos dados (1-6) 
y que muestre por pantalla el mensaje GANADOR cuando genere dados iguales,
de lo contrario, el mensaje dirá, SIGUE INTENTANDO.
'''

#Importar biblioteca para generar números aleatorios enteros.
from random import randint

#Función para lanzar y generar los valores de los dos dados.
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

#Salidas
d = dices()
d1 = d[0]
d2 = d[1]

print("Dices:", d)
print("Dice 1:", d1)
print("Dice 2:", d2)

if d1 == d2:
    print("Felicidades eres el Ganador")
else:
    print("Sigue intentando")