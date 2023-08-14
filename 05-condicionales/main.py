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

Operadores lógicos
and  a y b
or   a o b
not   no a
"""
print("########## Ejemplo 2 ##########")
year = 2023
if year > 2023:
    print("Ese año aun no llega.")
elif year <= 2023:
    print("Estás en el año 2023......o menos.")

print("########## Ejemplo 3 ##########")
#name = input("Escribe tu nombre: ")
name = "Alexis Arturo"
#city = input("Escribe tu ciudad: ")
city = "Yautepec"
#country = input("Escribe de que país eres: ")
country = "México"
#age = int(input("Escribe tu edad: "))
age = 18
adult = 18
if age >= adult:
    print(f"{name} eres mayor de edad.")
    if country != "México":
        print(f"El usuario {name} es extranjero.")
    elif country == "México":
        print(f"El usuario {name} es mexicano.")
        print(f"Eres de la ciudad {city}.")
else:
    print(f"El usuario {name}, tiene {age} años, no es mayor de edad.")

print("########## Ejemplo 4 ##########")
number_day = int(input("Escribe un número del 1 - 7: "))
if number_day == 1:
    print(f"El número {number_day} = Lunes")
elif number_day == 2:
    print(f"El número {number_day} = Martes")
elif number_day == 3:
    print(f"El número {number_day} = Míercoles")
elif number_day == 4:
    print(f"El número {number_day} = Jueves")
elif number_day == 5:
    print(f"El número {number_day} = Viernes")
elif number_day == 6: 
    print(f"El número {number_day} = Sabado")
elif number_day == 7:
    print(f"El número {number_day} = Domingo")
else:
    print("Número fuera de rango")

print("########## Ejemplo 5 ##########")

age_work = 18
full_age = 65
user_age = int(input("Ingresa tu edad: "))
if user_age < age_work :
    print(f"Eres menor de edad, no puedes trabajar.")
elif user_age >= age_work and user_age <= full_age:
    print(f"Tienes {user_age} años, puedes trabajar.")
elif user_age > full_age:
    print("Eres adulto mayor, no puedes trabajar.")