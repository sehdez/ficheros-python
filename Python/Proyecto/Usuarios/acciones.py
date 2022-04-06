from io import open_code
from os import system
import Notas.acciones as acciones
# Para ocultar la contraseña
import getpass
from Usuarios import usuarios
class Acciones():
    def menu(self):
        opcion = '0'
        while opcion != '1' or opcion != '2' or opcion != '3':
            system("cls")
            print("Bienvenido")
            print("1.- Iniciar Sesión")
            print("2.- Registrarse")
            print("3.- Salir")
            opcion = input("Seleciona una opcíon: ")
            if opcion == '1' or opcion == '2' or opcion =='3':
                return opcion
    def login(self):
            system("cls")
            print("Iniciar Sesión")
            email = input("Ingresa tu email: ")
            psw = getpass.getpass("Ingresa tu contraseña: ")
            persona = usuarios.Usuario('','',email,psw)
            login = persona.identificar()
            if login[0]:
                self.proccimasAcciones(login[1])



    def registro(self):
        opc = 1
        while opc:
            system ("cls")
            print("Registrate")
            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")
            email = input("Ingresa tu email: ")
            psw = getpass.getpass("ingresa tu contraseña: ")
            registro = usuarios.Usuario(nombre,apellido,email,psw)
            opc = registro.registrar()
    def proccimasAcciones(self,usuario):
        opc = "0"
        while opc != "4":
            system("cls")
            print(f"Bienvenido {usuario[1]} {usuario[2]}")
            print("Acciones disponibles:")
            print("1.- Crear nota")
            print("2.- Mostrar tus notas")
            print("3.- Eliminar notas")
            print("4.- Cerrar Sesión")
            opc = input("")

            hazEl = acciones.Acciones()
            if opc == "1":
                system("cls")
                
                hazEl.crear(usuario)


            elif opc == "2":
                system("cls")
                
                hazEl.mostrar(usuario)
            elif opc == "3":
                system("cls")
                print ("Eliminar nota: ")
                hazEl.eliminar(usuario)
            
