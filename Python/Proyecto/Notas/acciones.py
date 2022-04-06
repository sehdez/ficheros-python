from os import system
import Notas.nota as modelo
class Acciones():
    def crear(self,usuario):
        print(f"{usuario[1]}, vamos a crear una nueva nota")
        titulo = input("Introduce el título de la nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print("Nota creada con exito")
            system("pause")
        else:
            print("Ocurrió un problema y no se guardó la nota")
            system("pause")
        
        

    def mostrar(self,usuario):
        print(f"{usuario[1]} aquí están tus notas: \n")
        nota = modelo.Nota(usuario[0])
        lista = nota.listar()
        print(lista[0])
        system ("pause")

    def eliminar(self,usuario):
        system("cls")
        nota = modelo.Nota(usuario[0])
        lista = nota.listar()
        print(lista[0])
        slista = lista[1]
        try:
            borrar = int(input("Cuál de las siguientes notas quieres eliminar: "))
            if borrar > 0 and borrar <= len(slista):
                id =  slista[borrar-1]
                print(len(slista))
                print (nota.eliminar(id[0]))
            else: 
                print("La no ta que deseas eliminar, no existe")
            system("pause")
        except:
            print("Ingresaste un tipo de dato que no es entero")
            system("pause")
            borrar = 0
            self.eliminar(usuario)
        
        
        
        #id_nota = slista.index(borrar-1)
        #print(lista[1])
        #print (slista[borrar-1])
        
        