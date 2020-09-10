try:
    numero=int(input("Ingrese numero: "))
    print(f"El cuadrado es {numero*numero}")
except TypeError:
    print("Debes convertir tu cadena a entero")
except ValueError:
    print("El valor ingresado no es numerico")
except Exception as e:
    print("ha ocurrido un error: ",type(e).__name__)