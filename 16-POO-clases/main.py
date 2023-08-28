# Programación orientada a objetos

# Definir una clase (molde para crear obejtos de ese tipo con caracteristicas similares)
class Car:
    #atrubutos y propiedades (variables), caracteristicas del coche
    color = "Rojo"
    brand = "NISSAN"
    model = "370z"
    speed = 300
    horsepower = 480
    plazas = 2

    # Metodos son acciones que hace el objeto coche (funciones)
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setBrand(self, brand):
        self.brand = brand

    def getBrand(self):
        return self.brand
    
    def setPlazas(self, plazas):
        self.plazas = plazas
    
    def getPlazas(self):
        return self.plazas
        
    def setModel(self, model):
        self.model = model
    
    def getModel(self):
        return self.model
    
    def speedUp(self):
        self.speed +=  1

    def curp(self):
        self.speed -= 1

    def getSpeed(self):
        return self.speed
    # Fin definición clases

#Crear objetos / Instanciar la clase
print("#### Coche 1 ####")
car1 = Car()
print(f"Marca: {car1.brand}")
print(f"Modelo: {car1.model}")
print(f"Color: {car1.color}")
print(f"Velocidad: {car1.getSpeed()}")
car1.speedUp()
car1.speedUp()
print(f"Velocidad: {car1.getSpeed()}")
car1.curp()
print(f"Velocidad: {car1.getSpeed()}")
new_color = "Verde"
new_model = "GTR"
new_plazas = 1
car1.setColor(new_color)
car1.setModel(new_model)
car1.setPlazas(new_plazas)
print("######## Nuevo cambios al coche ########")
print(f"Nuevo color del coche: {car1.getColor()}")
print(f"Nuevo modelo del coche: {car1.getModel()}")
print(f"Nuevas plazas del coche: {car1.getPlazas()}")

print("#### Coche 2 ####")
car2 = Car()
car2.setColor("Negro")
car2.setBrand("INFINITI")
car2.setModel("QX55")

print(car2.getBrand())
print(car2.getModel())
print(car2.getColor())
print(car2.getPlazas())
print(car2.getSpeed())
