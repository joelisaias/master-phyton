import datetime
import hashlib
from usuarios import conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    #constructor
    def __init__(self,nombre,apellidos,email,password):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.password=password

    def registrar(self):
        fecha=datetime.datetime.now()
        #cifrar contraceña
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
        usuario=(self.nombre,self.apellidos,self.email,cifrado.hexdigest(),fecha)
        try:
            cursor.execute(sql,usuario)
            database.commit()
            return [cursor.rowcount,self]
        except Exception as e:
            print("Error al guardar: ", type(e).__name__)
            return [0,self]

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email=%s and password=%s"
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario=(self.email,cifrado.hexdigest())
        cursor.execute(sql,usuario)
        result = cursor.fetchone()
        return result