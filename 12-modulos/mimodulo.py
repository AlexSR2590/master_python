def greet(name):
    return f"Hola {name}, ¿Cómo estás?"

def multiplicationTable(number):
    result = f"------------ Tabla del {number} ------------\n"
    for i in range(1, 11):
        result += f"{number} x {i} = {number*i}\n"
    return result 

