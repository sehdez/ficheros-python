from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana,text="Bienvenido")
texto.config(
    # font color
    fg = "yellow",
    # background color
    bg = "#aaa",
    # Padding in x
    padx = 20,
    # Padding in y
    pady= 20,
    # Fuente
    font = ('Arial', 30)
)
texto.pack(fill= X, side = TOP)


texto = Label(ventana,text = "Básico1")
texto.config(
    height=3,
    bg = "green",
    padx = 10,
    pady= 20,
    font = ('Arial', 18)
)
texto.pack(side= LEFT, fill= X, expand= YES, anchor= N)


texto = Label(ventana,text = "Básico2")
texto.config(
    height=3,
    fg = "black",
    bg = "white",
    padx = 10,
    pady= 20,
    font = ('Arial', 18)
)
texto.pack(side=LEFT, fill= X, expand= YES,anchor= N)

texto = Label(ventana,text = "Básico3")
texto.config(
    height=3,
    bg = "red",
    padx = 10,
    pady= 20,
    font = ('Arial', 18)
)
texto.pack(side = LEFT, fill= X, expand= YES,anchor= N)




ventana.mainloop()