#LOS CONDICIONALES
'''
Pueden ser simples o compuestos / anidados
Es necesario usar tabla de operadores lógicos:
> => Mayor que
< => Menor que
>= => Mayor o igual que
<= => Menor o igual que
<> => Diferente de
!= => Diferente de
=  => Asignación
== => Igual a (Operador de comparación)
Se usan los valores o expresiones booleanas
'''
n1 = 10
if n1 > 0 : #True or False
    print("El número", n1, "es positivo")
elif n1 < 0 : 
    print("El número ", n1, " es negativo")
else :
    print("El valor es cero")
    