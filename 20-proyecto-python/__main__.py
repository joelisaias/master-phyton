from usuarios.acciones import Acciones

print("""
Acciones Disponibles:
    -registro
    -login
""")

hazEl = Acciones()

accion = input("¿Que quieres hacer?")
if accion == "registro":
    hazEl.registro()    
elif accion =="login":
    hazEl.login()