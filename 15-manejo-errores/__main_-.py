
try:
    nombre=input("¿Cual es tu nombre?")

    if len(nombre)>0:
        nombreusuario=f"El nombre es {nombre}"
    print(nombreusuario)
except:
    print("Ha ocurrido un error: ingresa e nombre")
else:
    print("Todo bien")
finally:
    print("Ya termino todo")

