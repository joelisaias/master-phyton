from io import open
import pathlib

import shutil

#abrir archivo

ruta=str(pathlib.Path().absolute())+"/14-sistema-archivos/fichero-texto.txt"
#print(ruta)

archivo=open(ruta,"a+")
#escribir en el archivo
archivo.write("********Soy un texto escrito desde Py*************\n")
#cerrar archivo
archivo.close()

#abrir archivo
archivo_lectura=open(ruta,"r")

#contenido=archivo_lectura.read()
#print(contenido)

#Leer contenido en lista
lineas = archivo_lectura.readlines()
archivo_lectura.close()
for linea in lineas:
    print(linea)



#copiar archivo
"""

rutaoriginal=str(pathlib.Path().absolute())+"/14-sistema-archivos/fichero-texto.txt"
rutanueva=str(pathlib.Path().absolute())+"/14-sistema-archivos/fichero-copiado.txt"
shutil.copyfile(rutaoriginal,rutanueva)

"""

#mover archivo
"""
rutaoriginal=str(pathlib.Path().absolute())+"/14-sistema-archivos/fichero-copiado.txt"
rutanueva=str(pathlib.Path().absolute())+"/14-sistema-archivos/fichero-nuevo.txt"
shutil.move(rutaoriginal,rutanueva)
"""

#eliminar
"""
import os

rutanueva=str(pathlib.Path().absolute())+"/14-sistema-archivos/fichero-nuevo.txt"
os.remove(rutanueva)
"""

#Comprobar si existe

from os import path

print(path.abspath('./'))
if path.isfile(path.abspath('./')+"/14-sistema-archivos/fichero-texto.txt"):
    print("el fichero existe")
else:
    print("el fichero no existe")



