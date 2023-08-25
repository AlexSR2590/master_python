"""
Crear una función que reciba una variable y que regrese el tipo de dato que es esa variable.
"""
def isType(variable):
    result = ""
    if isinstance(variable, int):
        result = f"La variable es un entero y su contenido es: \n{variable}"
    elif isinstance(variable, list):
        result = f"La variable es una lista y su contenido es: \n{variable}"
    elif isinstance(variable, float):
        result = f"La variable es un flotante y su contenido es: \n{variable}"
    elif isinstance(variable, bool):
        result = f"La variable es un booleano y su contenido es: \n{variable}"
    elif isinstance(variable, dict):
        result = f"La variable es un diccionario y su contenido es: \n{variable}"
    elif isinstance(variable, str):
        result = f"La variable es un string y su contenido es: \n{variable}"
    else:
        result = type(variable)
    return result

var_list = [1, 2, 3, 4, 5]
var_int = 33
var_float = 1.70
var_bool = True
var_dic = {
    "nombre" : "ALexis",
    "apellido" : "Solís",
    "correo" : "alex@gmail.com"
}
var_str = "Hola Mundo!!!"
print(isType(var_list))
print(isType(var_int))
print(isType(var_float))
print(isType(var_bool))
print(isType(var_dic))
print(isType(var_str))