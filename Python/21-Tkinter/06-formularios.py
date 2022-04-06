from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter")

# Encabezado 
encabezado = Label(ventana, text= "Fromularios con Tkinter")

encabezado.config(
    fg = "white",
    bg = "darkgray",
    font = ("Arial",18),
    bd= 2,
    relief="solid",
    padx= 10,
    pady= 10,
)

encabezado.grid(row=0, column= 0, columnspan= 2, sticky= W)

# Label para el campo
lNombre = Label(ventana, text="Nombre:")
lNombre.grid(row=1, column=0, pady=5, padx=5, sticky=W)
# Campo de texto
cajaTexto = Entry(ventana)
cajaTexto.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Label para la caja
lApellido = Label(ventana, text="Apellidos:")
lApellido.grid(row=2, column=0, pady=5, padx=5, sticky=W)
# Caja de texto
cajaTexto = Entry(ventana)
cajaTexto.grid(row=2, column=1,padx=5, pady=5, sticky=W )
# state es para desabilitar un campo, justify es donde comenzara el texto
cajaTexto.config(justify=LEFT, state="normal") 

# Label para la textArea
lDescripcion = Label(ventana, text="Descripción:")
lDescripcion.grid(row=3, column=0, pady=5, padx=5, sticky=N)
# Crear un TextArea
textoGrande = Text(ventana)
textoGrande.config(width=30, height=5)
textoGrande.grid(row=3, column=1,padx=5, pady=5, sticky=W)
# Crear separacion entre elementos
#Label(ventana).grid(row=4, column= 1)
boton = Button(ventana, text= "Enviar")
boton.grid(row=5,column=1,padx=5, pady=5, sticky=W )




ventana.mainloop()