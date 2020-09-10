import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='',
    database="master_phyton"
)


cursor=database.cursor(buffered=True)

# cursor.execute('create database if not exists master_phyton')
# cursor.execute('SHOW DATABASES')


# for db in cursor:
#     print(db)

#crear tabla

cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(ID)
)""")



#insert masivo
carros=[
    ('Ferrari','Aventador',250000),
    ('hyundai','Accent',20000),
    ('Nissan','Qashqai',30000),
]
"""
cursor.executemany("INSERT INTO VEHICULOS VALUES(null,%s,%s,%s)",carros)

database.commit()
print(cursor.rowcount,"Insertados!")
"""

cursor.execute("select marca,modelo from vehiculos")

listavehiculos=cursor.fetchall()

for vehiculo in listavehiculos:
    print("---------------------------------")
    print(f"marca: {vehiculo[0]}")
    print(f"modelo: {vehiculo[1]}")
    print("---------------------------------")


"""
#Eliminar registros
cursor.execute("delete from vehiculos")
database.commit()
print(cursor.rowcount,"Borrados!")

"""


cursor.execute('update vehiculos set modelo="Elantra" where marca="hyundai"')
database.commit()
print(cursor.rowcount,"Actualizados!")