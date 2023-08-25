"""
Hacer un programa que compruebe si una variable está vacia, 
si está vacia, llenarla con texto que el usuario ingrese por teclado,
mostrar por pantalla en mayusculas.
Si la variable tiene contenido, mostrar el contenido.
"""
def itsEmpty(variable):
    result = ""
    if variable:
        result = f"La variable tiene contenido: \n{variable}"
    else:
        text = input("La variable está vacia, ingrese un texto: ")
        result = text.upper()
    return result

variable = ""
variable2 = "Hola Mundo!!!"
print(itsEmpty(variable))
print(itsEmpty(variable2))