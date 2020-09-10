nombre="Joel Alvarado"

print(nombre)
print(type(nombre))

#detectar el tipado
comprobar=isinstance(nombre,int)

print(str(comprobar))

#limpiar espacios
frase="              Esta Frase Tiene espacios                  "
print(frase)
#del frase  #eliminar variable
print(frase.strip())

#longitud de caracteres
print(len(frase))

#buscar caracteres
print(frase.find('Tiene'))

#remplazar caracteres
print(frase.replace('Tiene','NO tiene Nada de'))

#mayusculas minusculas
print(frase.lower())
print(frase.upper())