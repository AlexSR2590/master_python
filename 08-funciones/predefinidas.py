#name = "Alexis Arturo Solís"
name = 33
# Funciones generales.
print(type(name))

# Detectar el tipado.
check_typing = isinstance(name, str)
if check_typing:
    print("La variable es un String")
else:
    print("La variable no es un String")

# Limpiar espacios en un string

text = "       Es te es un texto     con muchos espacios     1"
print(text)
print(text.strip())

# Eliminar variables

year = 2023
print(year)
del year
#print(year)

#Comprobar variables vacias
#phrase = "Hola mundo"
phrase = ""
if len(phrase) == 0:
    print("La variable está vacia.")
if len(phrase) > 0:
    print("La variable no está vacia.")

#Reemplazar la palabra en un string 
phrase = "La moto es negra"
print(phrase)
new_phrase = phrase.replace("moto", "camioneta")
print(new_phrase)

# Mayusculas y minusculas
print(phrase.upper())
print(phrase.lower())