import os
import shutil

if not os.path.isdir("./14-sistema-archivos/micarpeta"):
    os.mkdir("./14-sistema-archivos/micarpeta")
else:
    print("Dir ya existe")

#elimina carpeta
#os.rmdir("./14-sistema-archivos/micarpeta")


#Copiar carpeta
"""
ruta_original="./14-sistema-archivos/micarpeta"
ruta_nueva="./14-sistema-archivos/micarpetanueva"

shutil.copytree(ruta_original,ruta_nueva)

"""

print("contenido de carpeta")

contenidocarp=os.listdir("./14-sistema-archivos/micarpeta")

#print(contenidocarp)

for content in contenidocarp:
    print(content)
