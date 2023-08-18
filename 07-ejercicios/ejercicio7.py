"""
Hacer un programa que muestre todos los números 
impares entre los dos números que ingrese el usuario
"""
number1 = int(input("Escribe el primer número: "))
number2 = int(input("Escribe el segundo número: "))
if number1 <= number2:
    for i in range(number1, number2 + 1):
        if i % 2 != 0:
            print(f"Número impar: {i}")
elif number2 <= number1:
    for i in range(number2, number1 + 1):
        if i % 2 != 0:
            print(f"Número impar: {i}")
