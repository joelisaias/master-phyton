from coche import Coche

carro1=Coche('Azul','lamborgini','Gallardo',300,200,2)
carro2=Coche('Negro','Ford','Mustang',250,200,4)
carro3=Coche('Rojo','Ferrari','Aventador',290,250,2)
carro4=Coche('Amarillo','Chevy','Camaro',270,200,4)

print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

#Detectar tipado
if type(carro1) == Coche:
    print("Es un coche")
else:
    print("No es un coche")

print(carro1.atributopublico)
print(carro1.getAtributoPrivado())
