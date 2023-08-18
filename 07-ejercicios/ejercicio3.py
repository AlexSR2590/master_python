"""
Ejercicio 3
Escribir un programa que escriba en pantalla los cuadrados del 1 al 30
con el bucle for
con el bucle while
"""
print("######## Cuadrados del 1 al 60 con bucle for ########")
for i in range(1,31):
    print(f"Cuadrado del {i} = { i * i}")
print("-------------------------------------------")
print("######## Cuadrados del 1 al 60 con bucle while ########")
count = 1
while count <= 30:
    print(f"Cuadrado del {count} = { count * count}")
    count += 1