"""
Pedir dos números y mostrar las operaciones básicas
suma
resta
multiplicación
división
"""
print("Dame dos números para mostrar las operaciones básicas")
number1 = int(input("Escribe el primer número: "))
number2 = int(input("Escribe el segundo número: "))
if number1 < 0 and number2 < 0:
    print("Los números ingresados deben ser positivos")
elif number1 >= 0 and number2 >= 0 and number2 != 0:
    print(f"{number1} + {number2} = {number1 + number2}")
    print(f"{number1} - {number2} = {number1 - number2}")
    print(f"{number1} x {number2} = {number1 * number2}")
    print(f"{number1} / {number2} = {number1 / number2}")
else:
    print(f"{number1} + {number2} = {number1 + number2}")
    print(f"{number1} - {number2} = {number1 - number2}")
    print(f"{number1} x {number2} = {number1 * number2}")
    print(f"{number1} / {number2} = Error, No se puede didivir entre 0")