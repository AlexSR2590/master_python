# Capturar excepciones y manejo de errores en código susceptible a fallos
"""
try:
    name = input("Ingresa tu nombre: ")
    if len(name) > 1:
        user_name = f"El nombre es: {name}"
        
    print(user_name)
except:
    print("Ha ocurrido un error, introduce bien el nombre.")
else:
    print("Todo funcionó correctamente.")
finally:
    print("Fin del programa.")
"""

# Manejo de multiples excepciones
"""
try:
    number = int(input("Ingresa un número para hacer una operación: "))
    operation = number ** 2
    print(f"El cuadrado del {number} es: {operation}")
except ValueError:
    print("Debes ingresar números enteros.")
except Exception as e:
    print(f"Ha ocurrido un error: {type(e).__name__}")
"""
# Excepciones personalizadas o lanzar excepciones
try:
    name = input("Ingresa tu nombre: ")
    year = int(input("Ingresa tu edad: "))

    if year < 5 or year > 110:
        raise ValueError("La edad introducida no es real.")
    elif len(name) <= 1:
        raise ValueError("El nombre no está completo.")
    else:
        print(f"Bienvenido al master en python: {name}")
except ValueError:
    print("Introduce los datos correctamente.")
except Exception as e:
    print("Existe un error.")
