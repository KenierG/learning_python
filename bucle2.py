#Funcion para simular los intentos de ingreso de clave en cajero automatico.
#Intentos permitidos: 3
import os

os.system('clear')

def cajero():
    #Clave registrada en el banco
    my_clave_banco = '2024'

    cont_attempts = 1
    status = True

    #Clave que digito en el ATM
    while status:
        clave = input("Digita tu clave: ")
        if my_clave_banco == clave :
            print("Has ingresado a tu cuenta")
            print(f"Intento satisfactorio: {cont_attempts}")
            status = False #brake
        else :
            if cont_attempts < 3 :
                print(f"Intento {cont_attempts}: Clave incorrecta, intenta nuevamente.")
                cont_attempts += 1
            else:
                print(f"Intento {cont_attempts}: Clave incorrecta")
                cont_attempts += 1
            
            if cont_attempts > 3 :
                print("Se han agotados los intentos permitidos.\nTu cuenta ha sido bloqueada")
                break
    
cajero()