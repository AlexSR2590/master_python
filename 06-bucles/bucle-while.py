# Bucle while.
count = 0
while count <= 15:
    print(f"{count}")
    count += 1
print("-------------------------------------")
count = 1
multipli = int(input("De que número quieres la tabla de multiplicar: "))
if multipli <= 0:
    multipli = 1
while count <= 10:
    print(f"{multipli} x {count} = {multipli * count}")
    count += 1
