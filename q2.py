import random

def juego_de_numeros():
    print("¡Bienvenido al juego de números!")

    numero_secreto = random.randint(1, 100)

    intentos = 0
    adivinado = False

    print("Intenta adivinar el número entre 1 y 100.")

    while not adivinado:
        try:
            suposicion = int(input("Tu suposición: "))
            
            intentos += 1

            if suposicion == numero_secreto:
                adivinado = True
                print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            elif suposicion < numero_secreto:
                print("El número es mayor. Intenta nuevamente.")
            else:
                print("El número es menor. Intenta nuevamente.")

        except ValueError:
            print("Por favor, ingresa un número entero válido.")

juego_de_numeros()

