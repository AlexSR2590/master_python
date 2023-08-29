class Car():
    def __init__(self, color, brand, model, speed, horsepower, plazas):
        self.color = color
        self.brand = brand
        self.model = model
        self.speed = speed
        self.horsepower = horsepower
        self.plazas = plazas
        self.soy_publico = "Soy un atributo público"
        self.__privado= "Soy un atributo privado"

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setBrand(self, brand):
        self.brand = brand
    
    def getBrand(self):
        return self.brand
    
    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def getSpeed(self):
        return self.speed
    
    def setHorsepower(self, horseporwer):
        self.horsepower = horseporwer

    def getHorsepower(self):
        return self.horsepower
    
    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPlazas(self):
        return self.plazas
    
    def speedUp(self):
        self.speed += 1

    def curp(self):
        self.speed -= 1
    
    def getDataCar(self):
        result = "---------- Información del automóvil ----------\n"
        result += f"Marca: {self.brand}\n"
        result += f"Modelo: {self.model}\n"
        result += f"Color: {self.color}\n"
        result += f"Plazas: {self.plazas}\n"
        result += f"Velocidad: {self.speed}\n"
        result += f"Caballaje: {self.horsepower}"
        return result
    
    def getPrivado(self):
        return self.__privado