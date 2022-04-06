from tkinter import *

ventana = Tk()
ventana.geometry("200x250")
ventana.resizable(0,0)
ventana.title("Calculadora|Sergio")
ventana.iconbitmap("./Imagenes/cal.ico")

formulario = Frame(ventana, width=190, height=240)
formulario.config(bd=1, relief = "solid", bg="#ABBEEE")
formulario.pack(pady=5, padx=5)

ventanaTexto = Entry(formulario)
#ventanaTexto.config(width=28,)
ventanaTexto.grid(row =0, column=0, columnspan=4,padx=5, pady=5, sticky= N)

b9 = Button(formulario,text= 9).grid(row= 1, column= 0, padx=5, pady=5, sticky=W) 
b8 = Button(formulario,text= 8).grid(row= 1, column= 1, padx=5, pady=5, sticky=W) 


ventana.mainloop()

