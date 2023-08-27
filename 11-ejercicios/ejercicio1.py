"""
Ejercicio 1: Hacer un programa que tenga una lista de 8 números enteros y hacer lo siguiente
- Recorrer la lista y mostrarla (en una función)
- Ordenar la lista y mostrarla
- Mostrar su longitud de la lista
- Buscar algun elemento que el usuario ingrese por teclado
"""
print("###### Ejercicio 1 ######\n")
numbers = [ 8, 6, 1, 9, 7, 5, 2, 3]
# Recorrer la lista y mostrarla (en una función)
def showList(numbers_list):
    result = ""
    for number in numbers_list:
        result += str(number) + ", "
    return result
print("Recorrer la lista y mostrarla con una función.")
print(showList(numbers))
print("\nOrdenar la lista y mostrarla.")
numbers.sort()
print(numbers)
print("\nMostrar la longitud de la lista.")
print(len(numbers))
print("\nBuscar algún elemento que el usuario ingrese por teclado.")
try:
    number = int(input("Ingresa el número para buscar en la lista: "))
    if number in numbers:
        print(f"El número existe en la posición: {numbers.index(number) + 1} ")
    else:
        print("El número ingresado no se encuentra en la lista.")
except:    
    print("Error....Ingresa números enteros.")