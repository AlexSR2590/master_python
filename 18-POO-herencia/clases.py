# Herencia: es la posibilidad de compartir atributos y metodos y que diferentes clases hereden de otras
class Person():

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setLastName(self, lastName):
        self.lastName = lastName
    
    def getLastName(self):
        return self.lastName
    
    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def talk(self):
        return "Estoy hablando..."
    
    def walk(self):
        return "Estoy caminando"
    
    def sleep(self):
        return "Estoy durmiendo..ZzZzZz"
    
class Informatico(Person):
    def __init__(self):
        self.languages = ["Python", "JavaScript", "HTML", "MYSQL"]
        self.experience = 5
    
    def getLanguages(self):
        return self.languages
    
    def learnLanguages(self, language):
        self.languages.append(language)
        return self.languages
    
    def fixComputer(self):
        return "Estoy reparando la computadora"
    
    def program(self):
        return "Estoy programando"

class NetworkTechnician(Informatico):
    def __init__(self):
        super().__init__() # Para poder usar el constructor de la clase padre (Informatico)
        self.audit_networks = "Experto en redes"
        self.experience = 15

    def networkAudit(self):
        return "Estoy auditando una red."