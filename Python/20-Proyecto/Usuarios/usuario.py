import conexion 
import datetime
import hashlib

conectar = conexion.conectar()
database = conectar[0]
cursor = conectar[1]


cursor = database.cursor(buffered=True)

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email= email
        self.password = password



    def registrar(self):
        # CIFRAR LA CONTRASEÑA
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))


        fecha = datetime.datetime.now()
        try:
            
            sql = "INSERT INTO usuarios VALUES (null,%s,%s,%s,%s,%s)"
            usuario = (self.nombre,self.apellido,self.email,cifrado.hexdigest(),fecha)

            cursor.execute (sql,usuario)
            database.commit()
            resultado = [cursor.rowcount, self]
        except:
            resultado = [0,self]
        return resultado


    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.email,cifrado.hexdigest())
        cursor.execute (sql,usuario)
        result = cursor.fetchone()
        return result
