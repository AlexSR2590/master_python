# Predefined functions for lists
colors = ["Rojo", "Verde", "Blanco", "Amarillo", "Azúl"]
numbers = [1, 9, 5, 3, 7, 11, 6, 8]

# Ordenar 
print(numbers)
numbers.sort()
print(numbers)

# Añadir elementos
print("\n")
print(colors)
colors.append("Morado")
colors.insert(0, "Negro")
print(colors)

# Eliminar elementos
colors.pop(4)
colors.remove("Blanco")
print(colors)

# Invertir listas
print(numbers)
numbers.reverse()
print(numbers)

# Buscar dentro de una lista
print("Negro" in colors)

# Contar elementos
print(len(colors))

# Cuantas veces aparece un elemento en la lista
numbers.append(8)
print(numbers.count(8))

# Conseguir indice
print(colors.index("Azúl"))

# Unir listas
colors.extend(numbers)
print(colors)