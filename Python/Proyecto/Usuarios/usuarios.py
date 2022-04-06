from os import system
import Usuarios.conexion as conexion
import datetime
# Para encriptar la contraseña
import hashlib
# Excepción en caso de que no se pueda conectar a la base de datos
try:
    conectar = conexion.conectar()
    database = conectar[0]
    cursor = conectar[1]
except:
    print("El programa no se pudo conectar a la base de datos, favor de verificar el servidor")
    exit()

class Usuario:
    def __init__(self, nombre, apellido, email, psw):
        self.nombre = nombre
        self.apellido = apellido
        self.email= email
        self.psw = psw
    def identificar (self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cifrado = hashlib.sha256()
        cifrado.update(self.psw.encode('utf8'))
        usuario = (self.email, cifrado.hexdigest())
        cursor.execute(sql,usuario)
        if cursor.rowcount == 0:
            print("El usuario o la contraseña no son correctos")
            system("pause")  
            return[0,""]
        else:
            consulta = cursor.fetchone()
            print (f"Bienvenido {consulta[1]} te registraste el {consulta[5]}")
            system("pause") 
            return [1,consulta]
    def registrar(self):
        try:
            # CIFRAR LA CONTRASEÑA
            cifrado = hashlib.sha256()
            cifrado.update(self.psw.encode('utf8'))
            fecha = datetime.datetime.now()
            sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
            nuevoUsuario= (self.nombre,self.apellido,self.email,cifrado.hexdigest(),fecha)
            cursor.execute(sql,nuevoUsuario)
            database.commit()
            print (f"{self.nombre} te has registrado con el email {self.email}")
            system("pause")
            return 0
        except Exception as e :
            print("El email ya existe prueba con otro")
            system("pause")    
            return 1