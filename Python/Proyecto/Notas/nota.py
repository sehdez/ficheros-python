from os import system
import Usuarios.conexion as conexion


conectar = conexion.conectar()
database = conectar[0]
cursor = conectar[1]



class Nota:

    def __init__(self, usuario_id, titulo= "", descripcion= ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES (null,%s,%s,%s,NOW())"
        nota = (self.usuario_id,self.titulo,self.descripcion)
        cursor.execute(sql,nota)
        database.commit()
        return [cursor.rowcount, self]

    def listar (self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        cursor.execute (sql)
        result = cursor.fetchall()
        notas = ""
        for i in result:
            notas += f"{result.index(i)+1}: {i[2]}:\n{i[3]}\nCreada: {i[4]}\n\n"
        return [notas,result]

    def eliminar(self,id_nota):
            sql = f"DELETE FROM notas WHERE usuario_id= {self.usuario_id} AND id =  {id_nota}"
            cursor.execute(sql)
            database.commit()
            result = "Nota eliminada con exito"
            return result
