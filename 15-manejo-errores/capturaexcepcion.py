numeros=[1,4,6,8]

try:
    busqueda=int(input("Buscar numero: "))
    search=numeros.index(busqueda)
    print(f"El indice es {search}")
except:
    print("El numero no existe")