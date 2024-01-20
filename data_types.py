#Tipos de datos en Python
#Python es un lenguaje dinámicamente tipado
#Python es un lenguaje INTERPRETADO **

#1. Numéricos
##Enteros Z => int
num1 = 42
print("Num1: ", type(num1))
##Flotantes o decimales (reales) => float
num2 = 50.5
print("Num2: ", type(num2))
#Complejos => complex
num3 = 2j
print("Num3: ", type(num3))

#2. Cadena => String => str
my_name = "J"
print("my_name", type(my_name))
my_lastname = 'Ayala'
print("my_lastname", type(my_lastname))
profile = '''
    Joan es una persona enfocada
    en el trabajo de equipos.'''
address = 'Mz C casa 860 - Cod Post 520001'
print("address", type(address))
phone_number = "573006565366"
print("phone_number", type(phone_number))
print("profile", type(profile))

a = 1
b = 1
suma1 = a + b #Suma artimética

c = "1"
d = '301'
suma2 = c + d #Suma de cadenas (concatenación)

#suma3 = a + c
print("Suma1:", suma1) #2
print("Suma2:", suma2) #11
#print("Suma3:", suma3) #Error

#3. Lógicos (Valores o expresiones booleanas)
usuario_activo = True
print("usuario_activo", type(usuario_activo))
pago_realizado = False
print("pago_realizado", type(pago_realizado))

#4. Listas
frutas = ['Apple', 'Banana']
colors = ['Blue', 'Red', 'White', 'Green', 'Brown']
detodito = ["Joan", 20, 500000, 'Santa Mónica', 1.70, 60.0]
print(frutas)
print("frutas", type(frutas))
print(colors)
print("colors", type(colors))

print(detodito)
print("detodito", type(detodito[4]))
#5. Tuplas
#6. Diccionarios
#7. Conjuntos
