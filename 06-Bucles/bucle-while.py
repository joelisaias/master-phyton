contador=1
while contador<=100:
    print(f"Estoy en el bucle {contador}")
    contador+=1


contador=1
cadena=str(0)
while contador<=100:
    cadena=cadena+" , "+str(contador)
    contador+=1
print(cadena)


print("*****************************************")
print("Ejercicio Tabla While")

tabla=int(input('Ingrese el numero de tabla: '))

contador=1
while contador<=12:
    print(f"{tabla} x {contador} es : {tabla*contador}")
    contador+=1


