from io import open
import pathlib
import shutil

# Abrir archivo
route = str(pathlib.Path().absolute())+"/ficheros_texto.txt"
archive = open(route, "+a")
#print(f"Ruta absoluta: {route}")

#Escribir dentro de un archivo
#archive.write("##### Texto ingresado desde Python #####\n")

#Cerrar archivo
archive.close()

route = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
read_file = open(route, "r")

# Leer contenido
#content = read_file.read()
#print(content)

# Leer contenido y guardarlo en lista
list_content = read_file.readlines()
read_file.close()

for line_text in list_content:
    #list_text = line_text.split()
    print(f".- {line_text.center(100)}")

# Copiar un archivo
"""
original_route = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
new_route = str(pathlib.Path().absolute())+"/fichero_copiado.txt"
shutil.copyfile(original_route, new_route)
"""
# Mover un archivo
"""
original_route = str(pathlib.Path().absolute())+"/fichero_copiado.txt"
new_route = str(pathlib.Path().absolute())+"/fichero_renombrado.txt"
shutil.move(original_route, new_route)
"""
# Eliminar archivos
import os
#new_route = str(pathlib.Path().absolute())+"/fichero_renombrado.txt"
#os.remove(new_route)

# Comprobar si existe un fichero
import os.path 
absolute_path = os.path.abspath("./")
#print(absolute_path)
check_route = os.path.abspath("./")+"/ficheros_texto.txt"
print(check_route)
if os.path.isfile(check_route):
    print("El archivo existe.")
else:
    print("El fichero no existe.")