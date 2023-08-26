import os, shutil

# Comprobar si existe carpete y crearla sino existe

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("Carpeta creada.")
else:
    print("El directorio 'mi_carpeta' ya existe.")

# Copiar
original_path = "./mi_carpeta" 
new_path = "./mi_carpeta_copiada"
if os.path.isdir("./mi_carpeta_copiada"):
    print("El directorio 'mi_carpeta_copiada' ya existe.")
else:
    shutil.copytree(original_path, new_path)

# Eliminar carpeta
"""
if os.path.isdir("./mi_carpeta_copiada"):
    os.rmdir("./mi_carpeta_copiada")
    print("Directorio eliminado.")
else:
    print("El direcotrio no existe.")
"""
# Listar contenido de carpeta
print("Contenido de mi carpeta:")
content = os.listdir("./mi_carpeta_copiada")
for directories in content:
    print(directories)
