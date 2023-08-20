"""
Funciones.
"""
# Ejemplo 1
print("######### Ejemplo 1 primera función ########")
def showNames():
    print("Alexis")
    print("Andrea")
    print("Alejandro")
    print("Alexa")
    print("Carlos")
    print("Angel")
    print("\n")

showNames()
print("######### Ejemplo 2 función ########")
def showMyName(name, age):
    if age < 18:
        result = f"Hola {name} eres menor de edad."
    else:
        result = f"Hola {name} eres mayor de edad."
    return result
"""
my_name = input("Escribe tu nombre: ")
my_age = int(input("Escribe tu edad: "))
"""
my_name = "Andi"
my_age = 23
print(showMyName(my_name, my_age))

print("\n######### Ejemplo 3 función ########")
def multiplicationTable(number):
    result = f"###### Tabla de multiplicar del {number} ######\n"
    for i in range(1,11):
        result += f"{number} x {i} = {str(number * i)}\n"
    return result
#number_to_multiply = int(input("Ingresa el número de la tabla de multiplicar: "))
#print(multiplicationTable(number_to_multiply))
for number_table in range(1,11):
    print(multiplicationTable(number_table))

print("\n######### Ejemplo 4 función ########")
#Parametros opcionales
def getEmployee(employee_name, ine = None):
    result = "Empleado:\n"
    result += f"Nombre: {employee_name}\n"
    if ine == "":
        result += "INE: No registrado."
    else:
        result += f"INE: {ine}"
    return result

employee_name = input("Ingresa tu nombre: ")
employee_ine = input("Ingresa el INE: ")
print(getEmployee(employee_name, employee_ine))