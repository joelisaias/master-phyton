"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos en formato clave - valor
Es parecido a un array asociativo o un json
"""

persona={"nombre":"Joel","apellido":"Alvarado","edad":30}

print(type(persona))
print(persona)
print(persona['nombre'])

#Lista de diccionarios

contactos=[
    {"nombre":"Joel","apellido":"Alvarado","edad":30},
    {"nombre":"Ruth","apellido":"Alvarado","edad":27},
    {"nombre":"Milagro","apellido":"Alvarado","edad":21},
    {"nombre":"Nathaly","apellido":"Colcha","edad":27},
]

print(contactos)
print(contactos[2]['edad'])

for contacto in contactos:
    print(contacto['nombre'])