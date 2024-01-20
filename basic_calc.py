#Script title: Basic calculator v1
''' Developer name: Joan C. Ayala
Date: 18-01-2024 '''

'''Description: 
This calculator let you get the result of 4 basic 
math operations from two numbers (Variables).
'''

#INPUTS (two static variables)
num1 = 20
num2 = 3

#PROCESS
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

#OUTPUTS
print("::: BASIC CALC V1.0 :::")
print("Number 1: ", num1, type(num1))
print("Number 2: ", num2, type(num2))
print("The addition is: ", add, type(add))
print("The subtraction is: ", sub, type(sub))
print("The multiplication is: ", mul, type(mul))
print("The division is: ", div, type(div))
print("\n")
print("::: BASIC CALC V1.1 :::")
print("Number 1: ", num1)
print("Number 2: ", num2)
print("The addition is: ", num1+num2)
print("The subtraction is: ", num1-num2)
print("The multiplication is: ", num1*num2)
print("The division is: ", num1/num2)