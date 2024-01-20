'''Crear una calculadora que reciba dos valores
por consola, y realice las operaciones aritméticas básicas'''

import os

os.system('clear')

#inputs
print("Ingrese primer valor: ")
n1 = int(input())
n2 = int(input("Ingrese el segundo valor: \n"))
suma = n1 + n2
print("Suma:", suma)

print(type(n1))