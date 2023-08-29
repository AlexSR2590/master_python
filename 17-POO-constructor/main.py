from coche import Car

carro1 = Car("Gris", "INFINITI", "QX55", 350, 400, 5)
print("#### Carro 1 creado con la clase Car ####")
print(f"{carro1.getDataCar()}")

carro2 = Car("Azúl", "NISSAN", "Maxima", 315, 385, 4)
print("\n#### Carro 2 creado con la clase Car ####")
print(f"{carro2.getDataCar()}")

carro3 = Car("Verde", "Honda", "TYPE R", 360, 405, 2)
print("\n#### Carro 3 creado con la clase Car ####")
print(f"{carro3.getDataCar()}")

carrito = 33
# Detectar tipado
if type(carro3) == Car:
    print("Es un objeto tipo Car")
else:
    print("No es un objeto tipo Car")

# Visibilidad 
print(carro1.soy_publico) #Imprimiendo atributo público
print(carro1.getPrivado()) #Imprimiendo atributo privado