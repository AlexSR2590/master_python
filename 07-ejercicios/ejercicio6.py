"""
Hacer un script que muestra todas las tablas de multiplicar del 1 al 10
"""
count = 1
while count <= 10:
    print(f"###### Tabla de multiplicar del {count} ######")    
    for i in range(1,11):
        print(f"{count} x {i} = {count * i}")
    print("\n")
    count += 1