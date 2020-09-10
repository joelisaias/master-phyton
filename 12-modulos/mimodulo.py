def holamundo(nombre):
    return f"Hola que tal estas {nombre}"

def calculadora(numero1,numero2,basicas=False):
    ressuma=numero1+numero2
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