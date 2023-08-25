"""
Ejercicio 2. Escribir un programa que añada valores a una lista, mientra que su longitud
sea menos que 120 usar while y for.
"""

numbers = []
# Bucle while
print("Con bucle while.")
count = 1
while len(numbers) < 119:
    numbers.append(count)
    count += 1
print(numbers)

# Bucle for
numbers = []
print("\nCon bucle for.")
for number in range(1,120):
    numbers.append(number)
print(numbers)
