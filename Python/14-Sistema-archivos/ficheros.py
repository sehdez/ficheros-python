from io import open
import pathlib


#Para copiar, mover y renombrar archivos
import shutil

# Para eliminar ficheros
import os

"""
# Abrir un archivo
#Ruta absoluta
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta , "a+")
print(ruta)

# Escribir
archivo.write("*****Hola Mundo*****\n")

# Cerrar
archivo.close()

# Abrir archivo

archivo_lectura = open (ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()
#print (contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

#Mostrar la lista
for elemento in lista:
    print(elemento)

archivo_lectura.close()
"""


"""
# Copiar Arhcivo
rutaOriginal = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
rutaNueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
shutil.copyfile(rutaOriginal,rutaNueva)
"""

"""
ruta = str(pathlib.Path().absolute()) + "/mover/fichero_texto_copiado.txt"
rutaNueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.move(ruta, rutaNueva)
"""



"""rutaNueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"

# Eliminar archivo
#os.remove(rutaNueva)

# Comprobar si un archivo existe o no
import os.path
ruta = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta)

if os.path.isfile(ruta):
    print ("El archivo existe")
else:
    print("El archivo no existe")

"""


