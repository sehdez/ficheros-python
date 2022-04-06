import getpass
import logging
import Usuarios.usuario as modelo

class Acciones:

    def menu(self):
        print("""
        Selecciona un opción:
            1 - Registro
            2 - Login
        """)

        return input("")

    def registro(self):
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tus apellidos: ")
        email = input("Ingresa tu email: ")
        password = getpass.getpass("Ingresa tu contraseña")

        usuario = modelo.Usuario(nombre, apellido,email,password)
        
        registro = usuario.registrar()

        if registro[0] >= 1:
            print (f"Perfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}")

        else:
            print("No se regirstro correctamente")

    def login (self):
        print("Identificate")
        email = input("Ingresa tu email: ")
        password = getpass.getpass("Ingresa tu contraseña")

        usuario = modelo.Usuario ('','',email,password)
        login = usuario.identificar ()

        if email == login[3]:
            print (f"Bienvenido {login[1]}, te resgistrado en el sistema el día {login[5]}")
        else:
            print()





