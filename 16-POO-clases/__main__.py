
#Inicio definicion de clase
class Coche:
    #Atributos
    color = "Rojo"
    marca ="Ferrari"
    modelo = "Aventador"
    velocidad =300
    caballaje=500
    plazas=2

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
    

#Fin definicion de clase

#Crear objetos / Instanciar clase
coche=Coche()
print("-----------------------------------")
print("Coche 1")
print(coche.marca,coche.color,coche.modelo)
print(f"Velocidad actual: {coche.getVelocidad()}")
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print(f"Velocidad nueva: {coche.getVelocidad()}")

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print(coche.marca,coche.color,coche.modelo)
print("-----------------------------------")
print("Coche 2")
coche2=Coche()
coche2.setColor("Azul")
coche2.setModelo("Aventador")

print(coche2.marca,coche2.getColor(),coche2.getModelo())
