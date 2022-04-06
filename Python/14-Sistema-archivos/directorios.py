import os, shutil

#Crear carpeta
"""if not os.path.isdir("./Mi_carpeta"):
    os.mkdir("./Mi_carpeta")
    print("Carpeta Directorio creado")
else:
    print("El directorio ya existe")
"""


# Eliminar carpeta
#os.rmdir("./Mi_carpeta")

#Copiar Carpeta
"""ruta_original= "../Micarpeta_copiada"
ruta_nueva= "./Mi_carpeta_copiada"
shutil.move(ruta_original,ruta_nueva)
"""
#os.rmdir("./mover")

# Listar archivos de la carpeta
print("Contenido de mi carpeta")
contenido = os.listdir("./Mi_carpeta")
for fichero in contenido:
    print(f"Fichero #{contenido.index(fichero)+1}: {fichero}")




