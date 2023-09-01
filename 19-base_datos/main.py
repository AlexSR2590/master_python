import mysql.connector 
# Conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# cursor para ejecutar las consultas
cursor = database.cursor(buffered=True) #Buffefred para limpiar el cursos de diferentes consultas que se han manejado

# Crear una base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# mostrar las bases de datos
"""
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
"""

# crea tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculos PRIMARY KEY(id)
)
""")

# Mostrar trabla
"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""

# Instar datos dentro de la tabla
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'INFINITI', 'Q55', 1599354)")

# Insertar datos al mismo tiempo
"""
cars = [
    ('SENTRA', '2023', 850000),
    ('NP300', '2024', 950000),
    ('ALTIMA', '2023', 900000),
    ('TIDDA', '2011', 95000)
]
cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", cars)
"""
# Mostrar datos de la tabla
print("---------- Todos los vehiculos guardados en la tabla. ----------")
cursor.execute("SELECT * FROM vehiculos")
for car in cursor:
    print(car)

print("\n---------- Vehiculos con un precio igual o menor de $900,000.00 pesos ----------")

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 900000")
for car in cursor:
    print(car)

print("\n---------- Modelos disponibles de los vehiculos. ----------")
cursor.execute("SELECT * FROM vehiculos")
models = cursor.fetchall() # Guardar en una variable el resultado de la consulta
for model in models:
    print(f"Modelo: {model[1]} ------> ${model[3]}")
# Guardar la ejecución de la consulta

# Sacar el primer registro de la tabla
print("\nSacar el primer registro de la tabla vehiculos")
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

# Eliminar un registro
#cursor.execute("DELETE FROM vehiculos WHERE marca = 'TIDDA'")
#print(cursor.rowcount, "BORRADOS....")
#database.commit()

# Actualizar
cursor.execute("UPDATE vehiculos SET marca = 'VERSA' WHERE marca = 'SENTRA'")
print(cursor.rowcount, "Registros Actualizados....")
database.commit()