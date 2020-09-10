print("###########Ejemplo 1 ####################")
#Definicion de funcion
def muestraNombre(nombre):
    print(f"Hola {nombre}")

#Invocacion de funcion
muestraNombre("Joel")
muestraNombre("Isaias")


#Parametros opcionales
print("###########Ejemplo 4 ####################")

def getEmpleado(nombre,identificacion=None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if identificacion!=None:
        print(f"Identificacion: {identificacion}")

getEmpleado('Joel','0926983099')
getEmpleado('Joel')

print("###########Ejemplo 5 ####################")
def suma(num1,num2):
    return num1+num2

print(suma(2,4))

def calculadora(numero1,numero2,basicas=False):
    ressuma=suma(numero1,numero2)
    resta=numero1-numero2
    multi=numero1*numero2
    division=numero1/numero2
    cadena=""

    cadena+=f"Suma: {str(ressuma)}\n"
    cadena+=f"Resta: {str(resta)}\n"
    if not basicas:
        cadena+=f"Producto: {str(multi)}\n"
        cadena+=f"Division: {str(division)}\n"

    return cadena

print(calculadora(5,2))
print(calculadora(5,2,True))



#funciones lambda
print("###########Ejemplo 8 ####################")

dime_el_anio=lambda year: f"El año es {year*2}"

print(dime_el_anio(2050))

    