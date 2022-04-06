from genericpath import isfile
import os,  shutil

from os import close, supports_bytes_environ, system



## Función Principal
def main():
    try:
        # Variable para las opciones de los menús
        opcion = 0
        # Un bucle while para mostrar el menú cuantas veces sea necesario
        while opcion != 4:
            os.system("cls")
            print("\n************* Bienvenido este es mi primer proyecto en Pyhon *************\n")
            
            # llamamos a la función menú del archivo mostrar
            menu()
            # almacenamos la opción del usuario
            opcion = int(input("Digita una opción: "))

            if opcion>0 and opcion < 3:
                archivo(opcion)
                os.system("pause")

            elif opcion == 3:
                opcionsub = 0

                while opcionsub != 10:
                    os.system("cls")
                    submenu()
                    opcionsub = int(input("Digita una opción: "))

                    if opcionsub>0 and opcionsub <=9:
                        subOpc(opcionsub) 

                    elif opcionsub == 11:
                        opcionsub = 10
                        opcion = 4
    except ValueError:
        print("Ingresaste un tipo de dato no admitido")
        os.system("pause")
        main()
    except OSError:
        print("No se puede eliminar el directorio porque tiene archivos dentro")
        system("pause")
        main()
    except Exception as e:
        print(type(e).__name__)
        os.system("pause")
        main()


# Funcion para mostrar el menú
def menu():
    print("1.- Mostrar tipos de datos en Python")
    print("2.- Mostrar estructuras if, for y while")
    print("3.- Opciones con directorios y archivos")
    print("4.- Salir")


# Función para el submenú (3)
def submenu():
    print("1.-  Crear directorio")
    print("2.-  Crear archivo")
    print("3.-  Agregar texto a un archivo (falta agregar multilineas)")
    print("4.-  Mostrar el texto de un archivo")
    print("5.-  Renombrar directorio")
    print("6.-  Renombrar archivo")
    print("7.-  Borrar directorio")
    print("8.-  Borrar archivo")  
    print("9.-  Listar Directorio Actual")
    print("10.- Regresar al menú anterior")
    print("11.- Salir")


# Mostrar Tipos de datos y estructuras (1,2)
def mostrarArchivo(opc):
    if opc == 1:
        archivo = open("./Paquetes/Archivos/mostrarTipos.txt", "r")
    else :
        archivo = open("./Paquetes/Archivos/mostrarEstructuras.txt", "r")
    
    contenidoPorLineas = archivo.readlines()
    contenido = ""
    for i in contenidoPorLineas:
        contenido = contenido + i
    archivo.close()
    return contenido

# Llama a la función para mostrar un archivo
def archivo(opc):
    print(mostrarArchivo(opc))

def crearDir():
    directorioNuevo = input("Ingresa el nombre del directoro: ")
    if not os.path.isdir(f"./Directorios-Archivos{directorioNuevo}"):
        os.mkdir(f"./Directorios-Archivos/{directorioNuevo}")
        print ("Directorio creado")
    else:
        print("El directorio ya existe")
    system("pause")

def crearArchivo():
    archivoNuevo = "./Directorios-Archivos/" + input("Ingresa la ruta o el nombre del archivo: ")
    if not os.path.isfile(archivoNuevo):
        archivoNuevo = open(archivoNuevo,"a+")
        print("Archivo creado con exito")
        archivoNuevo.close()
    else:
        print("El archivo ya existe")
    
    system("pause")
    
def agregarTexto():

    archivo = "./Directorios-Archivos/" + input("Ingresa la ruta o el nombre del archivo para escribir: ")
    if os.path.isfile(archivo):
        archivo= open(archivo,"w")
        print("Archivo encontrado")
        system("pause")
        system("cls")
        print("***Puedes agregar el texto que gustes, para finalizar escribe 'end'***")
        texto = ""
        textocompleto = texto + input("")
        archivo.write(textocompleto)
        archivo.close()
    else:
        print("No se encontró el archivo")
        system("pause")



def mostrarTexto():
    archivo = "./Directorios-Archivos/" + input("Ingresa la ruta o nombre del archivo: ")
    if os.path.isfile(archivo):
        print("Se encontró el archivo")
        archivo = open(archivo,"r")
        contenidoPorLineas = archivo.readlines()
        contenido = ""
        for i in contenidoPorLineas:
            contenido = contenido + i
        return contenido
    else:
        return "No se encontró el archivo"
    


def renombrarDir():
    directorio = "./Directorios-Archivos/"+ input("Ingresa el nombre del directorio a renombrar: ")
    if os.path.isdir(directorio):
        print("Directorio encontrado")
        nuevoNombre = "./Directorios-Archivos/" + input("Ingresa el nuevo nombre: ")
        shutil.move(directorio,nuevoNombre)
        print ("Se renombró correctamente el directorio")
    else:
        print("No se encontró el directorio")
    system("pause")

def renombrarArchivo():
    archivo = "./Directorios-Archivos/"+ input("Ingresa el nombre del archivo a renombrar: ")
    if os.path.isfile(archivo):
        print("Archivo encontrado")
        nuevoNombre = "./Directorios-Archivos/" + input("Ingresa el nuevo nombre: ")
        shutil.move(archivo,nuevoNombre)
        print ("Se renombró correctamente el Archivo")
    else:
        print("No se encontró el Archivo")
    system("pause")

def borarDir():
    dir = "./Directorios-Archivos/" + input("Ingresa el directorio a borrar:")
    if os.path.isdir(dir):
        os.removedirs(dir)
        print("Se eliminó correctamente el directorio")
    else: 
        print("No se encontró el directorio")
    system("pause")

def borrarArchivo():
    archivo = "./Directorios-Archivos/" + input("Ingresa el archivo a borrar:")
    if os.path.isfile (archivo):
        os.remove(archivo)
        print("Se eliminó correctamente el archivo")
    else: 
        print("No se encontró el archivo")
    system("pause")
def listar():
    print("Contenido: ")
    contenido= os.listdir("./Directorios-Archivos")
    print(contenido)
    for i in contenido:
        print (i)
    system("pause")



 
        
#Opciones del submenú
def subOpc(opc):
    if opc == 1:
        crearDir()
    elif opc == 2:
        crearArchivo()
    elif opc == 3:
        agregarTexto()
    elif opc == 4:
        print (mostrarTexto())
        system("pause")
    elif opc == 5:
        renombrarDir()
    elif opc == 6:
        renombrarArchivo()
    elif opc == 7:
        borarDir()
    elif opc == 8:
        borrarArchivo()
    elif opc == 9:
        listar()



 