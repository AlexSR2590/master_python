"""
Mostrar todos los números entre dos números que de el usuario
"""
print("Introduce dos números para mostrar la seríe entre esos dos números")
number1 = int(input("Escribe el primer número: "))
number2 = int(input("Escribe el segundo número: "))

if number1 <= number2:
    for i in range(number1, number2 + 1):
        print(f"{i}")
else:
    for i in range(number2, number1 + 1):
        print(f"{i}")