#declaracion de variables
nada = None
cadena = "El futuro es hoy viejo"
entero=99
flotante=99.4
booleano=True
lista=[1,5,"Hola"]
tupla=("Joel",30,"Hola")
diccionario={
    "nombre":"Joel",
    "apellido":"Alvarado",
    "edad":30,
}

rango=range(9)
dato_byte= b"Prueba"

#imprimir variable
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(tupla)
print(diccionario)
print(rango)
print(dato_byte)

#mostrar tipo de dato

print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(tupla))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

#convertir tipos de datos

texto="HOla soy un texto"
numero=55
print(texto+" "+str(numero))