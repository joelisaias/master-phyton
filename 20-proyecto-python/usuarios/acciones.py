from usuarios.usuario import Usuario
class Acciones:

    def registro(self):
        print("\nOk, Vamos a registrarte al sistema...")
        nombre =input("¿Cual es tu nombre?: ")
        apellidos =input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("introduce tu contraseña: ")
        usuario=Usuario(nombre,apellidos,email,password)
        registro=usuario.registrar()
        if registro[0] >=1:
            print(f"{registro[1].nombre} registrado correctamente")
        else:
            print(f"no registrado correctamente")
        

    def login(self):
        print("Ok!! Identificate en el sistema...")
        email = input("Introduce tu email: ")
        password = input("introduce tu contraseña: ")
        usuario=Usuario('','',email,password)
        login=usuario.identificar()
        if login != None:
            print(f"Bienvenido {login[1]}, has iniciado sesion correctamente")
            self.proximasAcciones(login)
        else:
            print("Usuario incorrecto")
    
    def proximasAcciones(self,usuario):
        print("""
        Acciones Disponibles
        - Crear Nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar Nota (eliminar)
        - Salir (salir)
        """)

        accion= input("¿Quer desesas hacer?")
        if accion == "crear":
            print("vamos a crear")
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("vamos a mostrar")
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salrr":
            print("Hasta Pronto")
            exit()
        
        return None
