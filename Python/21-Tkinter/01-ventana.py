# TKINTER Modulo para crear interfaces gráficas de usuario
from tkinter import *
import os.path



class Formulario:

    def __init__(self):
        self.titulo = "Programa"
        self.medida = "600x400"
        self.ruta = "./Imagenes/3.ico"
        self.rutaAlternativa = "./21-Tkinter/Imagenes/3.ico"
        self.resizable = False
    
    def cargar(self):
        # Crear una ventana raíz
        ventana = Tk()
        self.ventana = ventana
        # Titulo de la ventana
        ventana.title(self.titulo)
        #Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.ruta)
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.rutaAlternativa)
        # icono de la ventana
        ventana.iconbitmap (ruta_icono)
        # Cambio de tamaño de ventaja
        ventana.geometry(self.medida)
        # Mostrar texto 
        texto = Label(ventana,text = ruta_icono)
        texto.pack()
        # Bloquear tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1) #(eje y, eje x) true or false
        else:
            ventana.resizable(0,0)
        
    def agregarTexto(self):
        texto = Label(self.ventana ,text = "Hola Mundo")
        texto.pack()

    def mostrar (self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()



#Instanciar
programa = Formulario()


programa.cargar()
programa.agregarTexto()
programa.mostrar()