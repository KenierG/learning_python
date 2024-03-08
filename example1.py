def calcular_resultado(x, y):
    resultado = None

    if x > y and y != 0:
        resultado = x / y
    elif x < y or y == 0:
        resultado = x + y
    else:
        resultado = x * y

    return resultado

ejemplo_1 = calcular_resultado(10, 5)
ejemplo_2 = calcular_resultado(8, 0)
ejemplo_3 = calcular_resultado(3, 3)

print("Ejemplo 1: calcular_resultado(10, 5) =", ejemplo_1)
print("Ejemplo 2: calcular_resultado(8, 0) =", ejemplo_2)
print("Ejemplo 3: calcular_resultado(3, 3) =", ejemplo_3)
