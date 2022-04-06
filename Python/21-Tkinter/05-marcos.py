from tkinter import *

ventana = Tk()
ventana.title("Marcos | Chinesse")
ventana.geometry("750x500")

marcoPadre = Frame(ventana, width=250, height=250)
marcoPadre.config(
    # Borde
    bd=3,
    relief="solid"
)
marcoPadre.pack(side=TOP, anchor=N, fill = X,expand=YES)
marco = Frame(marcoPadre, width=50, height=250)
marco.config(
    bg="green"
)
marco.pack(side=LEFT,fill = X, expand=YES)
marco = Frame(marcoPadre, width=50, height=250)
marco.config(
    bg="white"
)
marco.pack(side=LEFT,fill = X, expand=YES)
marco = Frame(marcoPadre, width=50, height=250)
marco.config(
    bg="red"
)
marco.pack(side=LEFT,fill = X, expand=YES)
marcoPadre = Frame(ventana, width=250, height=250)
marcoPadre.config(
    # Borde
    bd=3,
    relief="solid"
)
marcoPadre.pack(side=TOP, anchor=S, fill = X,expand=YES)
marco = Frame(marcoPadre, width=50, height=250)
marco.config(
    bg="green"
)
marco.pack(side=LEFT,fill = X, expand=YES)
marco = Frame(marcoPadre, width=50, height=250)
marco.config(
    bg="white"
)
marco.pack(side=LEFT,fill = X, expand=YES)
marco = Frame(marcoPadre, width=50, height=250)
marco.config(
    bg="red"
)
marco.pack(side=LEFT,fill = X, expand=YES)
# Para que no se modifique el marco al momento de agregar un texto
marco.pack_propagate(False)
texto = Label(marco,text="Pedro")
texto.config(
    bg="red",
    fg="white",
    height= 10,
    width= 10,

)
texto.pack()
ventana.mainloop()