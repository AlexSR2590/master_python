# Condicional IF

# Ejemplo 1
print("########## Ejemplo 1 ##########")
color = "rojo"
#color = input("Adivina el color: ")
if color == "rojo":
    print("ADIVINASTE!!!")
    print("El color es ROJO.")
else:
    print("El color no es correcto.")


"""
Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor igual que
>= mayor igual que
"""
print("########## Ejemplo 2 ##########")
year = 2023
if year > 2023:
    print("Ese año aun no llega.")
elif year <= 2023:
    print("Estás en el año 2023......o menos.")