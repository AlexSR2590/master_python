"""
Un modulo son funcionalidades ya hechas para reutilizar.
https://docs.python.org/3/py-modindex.html documentación de modulos en python.
"""
# Importando modulo propio completo
#import mimodulo
# Importando unicamente una funcion de mi modulo
#from mimodulo import greet
# Importar todo el modulo
from mimodulo import *

print(multiplicationTable(5))
print(greet("Alexis Arturo"))

# Modulo de fecha
import datetime
print(datetime.date.today())
# Time stamp
print(f"Time stamp: {datetime.datetime.now().timestamp()}")

full_date = datetime.datetime.now()
print(f"Fecha completa: {full_date}")
print(f"Año: {full_date.year}")
print(f"Mes: {full_date.month}")
print(f"Día: {full_date.day}")
print(f"Hora: {full_date.hour}:{full_date.minute}:{full_date.second}")

custom_date = full_date.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Fecha personalizada: {custom_date}")

# Modulo de matemáticas
import math
print(f"Raíz cuadrada de 10: {math.sqrt(10)}")
print(f"Número pi: {math.pi}")
print(f"Redondear para arriba: {math.ceil(5.66489)}")
print(f"Redondear para abajo: {math.floor(5.66489)}")

# Modulo random
import random
print(f"Número aleatorio entre 10 y 30: {random.randint(10, 30)}")