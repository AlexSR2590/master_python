# Bucle for
count = 0
result = 0
for count in range (0,10):
    print(count)

# Ejemplo de tabla de multiplicar
multipli = int(input("De que número quieres la tabla de multiplicar: "))

if multipli <= 0:
    multipli = 1
else:
    print(f"###### Tabla de multiplicar del {multipli} ######")
    for i in range(1,11):
        print(f"{multipli} X {i} = {multipli * i}")

    