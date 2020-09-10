nombre=input("Introduce tu nombre: ")
edad=int(input("Introduce tu edad: "))

try:
    if edad<18 or edad>75 :
        raise ValueError('no tiene edad para trabajar')
    elif len(nombre)<=1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido {nombre}")
except ValueError as ve:
    print("Introduce los valores correctamente",ve)
except Exception as e:
    print("Ocurrio un error ", e)
