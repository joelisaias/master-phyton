rango=range(15)
resultado=0
for var in rango:
    print(f"voy por el {str(var)}")
    resultado+=var

print(resultado)

tabla=int(input('Ingrese el numero de tabla: '))

for numero_tabla in range(1,13):
    print(f"{tabla} x {numero_tabla} es : {tabla*numero_tabla}")
else:
    print('Fin de tabla')