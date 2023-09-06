# Importar modulo para base de datos
import sqlite3

# Conexión 
connection = sqlite3.connect('./19-base_datos/pruebas.db')

# Crear cursor
cursor = connection.cursor()

# Crear una tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")

# Guardar cambios
connection.commit()

# Insertar un dato
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
connection.commit()
"""

# Borrar registros
"""
cursor.execute("DELETE FROM productos") # Elimina todos los registros de la tabla
connection.commit()
"""

# Insertar muchos registros al mismo tiempo
"""
products_list = [
    ("Computadora", "Escritorio", 10000),
    ("Tablet", "Lenovo", 2000),
    ("Smarth-Phone", "XIAOMI", 800),
    ("Laptop", "hp", 1500)
]
cursor.executemany("INSERT INTO productos VALUES(null, ?, ?, ? )", products_list)
connection.commit()
"""

# Actualizar registro (Update)
cursor.execute("UPDATE productos SET precio = 8356  WHERE precio = 800")
connection.commit()

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 2000")
products = cursor.fetchall()
#print(products)
for product in products:
    print(f"Id: {product[0]}")
    print(f"Título: {product[1]}")
    print(f"Descripción: {product[2]}")
    print(f"Precio: {product[3]}")
    print("\n")

# Mostrar el primer producto obtenido de la consulto
cursor.execute("SELECT * FROM productos")
product = cursor.fetchone()
print(f"Primer producto de la consulta: {product}")

# Cerrar conexión
connection.close()