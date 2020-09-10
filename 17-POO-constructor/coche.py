#Inicio definicion de clase
class Coche:
    #Atributos
    color = "Rojo"
    marca ="Ferrari"
    modelo = "Aventador"
    velocidad =300
    caballaje=500
    plazas=2

    atributopublico="soy attr publico"
    __atributoprivado="soy attr privado"

    #constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas        

    #metodos
    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

    #getter y setter    
    def getVelocidad(self):
        return self.velocidad

    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    
    def setMarca(self,marca):
        self.marca=marca
    def getMarca(self):
        return self.marca

    def getAtributoPrivado(self):
        return self.__atributoprivado

    def getInfo(self):
        info= " --- informacion del coche---\n"
        info+= f" Color: {self.getColor()}\n"
        info+= f" Marca: {self.getMarca()}\n"
        info+= f" Modelo: {self.getModelo()}\n"
        info+= f" velocidad: {int(self.getVelocidad())}\n"
        return info