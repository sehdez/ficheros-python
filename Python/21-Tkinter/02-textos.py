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
texto.pack()

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"


texto = Label(ventana,text=pruebas(nombre= "Sergio", apellidos = "Hernández",pais = "México"))
texto.config(
    fg = "red",
    bg = "green",
    padx = 10,
    pady= 10,
    font = ('Arial', 10),
    #justificar el texto
    justify= RIGHT,
    # orientación, la tenemos que escribir en el pack( anchor = E)
    #anchor= E

    # Modifica el ícono del cursor
    cursor="spider"
)
texto.pack(anchor= N)


ventana.mainloop()