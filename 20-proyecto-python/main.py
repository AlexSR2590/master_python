"""
Proyecto: Asistente de notas Python y Mysql.
- Abrir asistente.
- Login o Registro.
- Registro: creará un usuario en la base de datos.
- Login: Identificará al usuario 
- Crear, mostrar, editar y eliminar nota.
"""
from usuarios import acciones
print("""
Acciones disponibles:
    - Registro
    - Login
""")
make_the = acciones.Acciones()
action = input("Escribe la accion que deseas realizar: ").lower()
if action == "registro":
    make_the.register()
elif action == "login":
    make_the.login()
else:
    print("Ingresa los datos correctos.")
