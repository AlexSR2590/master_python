"""
Hacer un script que pida al usuario un número indefinidamente
hasta que el usuario ingrese el número 111
mostrar en pantalla cada número ingresado
"""
number = 0
while number != 111:
    number = int(input("Introduce el número 111 para finalizar el programa: "))
    print(f"{number}")