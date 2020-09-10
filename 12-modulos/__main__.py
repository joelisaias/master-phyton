#import mimodulo

"""
from mimodulo import calculadora
from mimodulo import holamundo
"""

from mimodulo import *

print(holamundo('Joel'))
print(calculadora(2,5))
print(calculadora(2,5,True))

#modulo de fechas

import datetime

print(datetime.date.today())

fechacompleta=datetime.datetime.now()


print(fechacompleta)
print(fechacompleta.year)
print(fechacompleta.month)
print(fechacompleta.day)
print(fechacompleta.weekday())
print(fechacompleta.hour)
print(fechacompleta.minute)
print(fechacompleta.second)

fechapersonalizada=fechacompleta.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Mi fecha personalizada es {fechapersonalizada}")

print(datetime.datetime.now().timestamp())



#Modulo matematicas

import math


print(f"La raiz cuadrada de 10: {math.sqrt(10)}")
print(f"Phi: {math.pi}")
print(f"Redondear arriba: {math.ceil(6.541215646)}")
print(f"Redondear abajo: {math.floor(6.541215646)}")

#Modulo random

import random
print(f"Numero random: {random.randint(35,67)}")
