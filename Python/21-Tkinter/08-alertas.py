from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("250x300")


def sacarAlerta():
    MessageBox.showinfo("Alerta", "Soy una puta Alerta xD")

btn1 = Button(ventana, text = "Mostrar alerta" ,command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Seguro que desea salir?")
    if resultado == "yes":
        MessageBox.showinfo("Adios",f"Nos vemos Pronto {nombre}")
        ventana.destroy()
btn1 = Button(ventana, text = "Salir" ,command=lambda: salir("Chino")).pack()


ventana.mainloop()