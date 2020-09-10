import sqlite3

#conexion
conexion=sqlite3.connect('pruebas.db')

cursor=conexion.cursor()

#crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo varchar(255),
descripcion text,
precio int(20)
)"""
)


conexion.commit()
#insertar
"""
cursor.execute("INSERT INTO productos values(null,'Segundo Producto', 'Teclado Corsair',1550)")

conexion.commit()
"""

#borrar
"""
cursor.execute("delete from productos")
conexion.commit()
"""

produtosInsert=[
    ("Monitor ultrawide","Monitor",2500),
    ("Teclado Mecanico","Teclado corsair",2500),
    ("Deck El Gato","Stream Deck",2500),
    ("Panasonic camera","Camara 4k",2500),
]

cursor.executemany("INSERT INTO productos values(null,?,?,?)",produtosInsert)
conexion.commit()


cursor.execute("update productos set titulo='El Gato Stream Deck' where id=13")
conexion.commit()

cursor.execute("Select * from productos")

productos=cursor.fetchall()

print(productos)

for producto in productos:
    print('---------------------------------------------')
    print('Id: ',producto[0])
    print('Titulo: ',producto[1])
    print('Descripcion: ',producto[2])
    print('Precio: ',producto[3])
    print('---------------------------------------------')


cursor.execute("Select descripcion from productos")

producto=cursor.fetchone()
print(producto)

#cerrar la conexion
conexion.close()