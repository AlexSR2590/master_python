"""
Calcular el x porciento de x número
Ejemplo: 20% de 150
"""
number = int(input("Introduce el número para obtener el porcentaje: "))
percentage = int(input("Introducel el porcentaje a obtener: "))
result = (number * percentage)/100
print(f"El {percentage}% de {number} es: {result}")