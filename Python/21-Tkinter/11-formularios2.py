from tkinter import *

ventana= Tk()
ventana.geometry("800x500")
encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    pady=15,
    padx=15,
    fg= "white",
    bg="green",
    font= ("Consolas",20)
)

# Funciones para el check
encabezado.grid(row =0, column=0, columnspan=5, sticky=W)
def mostrarProfesion():
    texto = ""
    if web.get():
         texto +="Desarrollo Web"
    if movil.get():
        if web.get():
            texto += " Y Desarrollo Movil"
        else:
            texto += "Desarrollo Movil"

    
    mostrar.config(text= texto, bg="green",fg="white")


# Botones check
web = IntVar()
movil = IntVar()
Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0,sticky=W)
Checkbutton(
    ventana, 
    text="Desarrollo web",
    variable= web,
    onvalue=1,
    offvalue= 0,
    command= mostrarProfesion
    ).grid(row=2,column=0, sticky=W)
Checkbutton(
    ventana, 
    text="Desarro movil",
    variable= movil,
    onvalue=1,
    offvalue= 0,
    command= mostrarProfesion
    ).grid(row=3,column=0, sticky=W)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0,sticky=W)

# Radio buttons
def marcar():
    marcado.config(text= opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana,text="¿Cuál es tu genero?").grid(row=5,sticky=W)
Radiobutton(
    ventana, 
    text="Masculino",
    variable=opcion,
    value="Masculino",
    command=marcar
    ).grid(row=6, sticky=W)
Radiobutton(
    ventana, 
    text="Femenino",
    variable=opcion,
    value="Femenino",
    command= marcar
    ).grid(row=7, sticky=W)

marcado = Label(ventana)
marcado.grid(row=8,sticky=W)


# Option menu
opc = StringVar()
opc.set("Opcion 1")

def seleccionar():
    seleccion.config(text= opc.get())

Label(ventana,text="Selecciona una opción").grid(row=9, sticky=W)
select = OptionMenu(ventana,opc,"Opcion 1","Opcion 2","Opcion 3")
select.grid(row=10, sticky=W)
seleccion = Label(ventana)
seleccion.grid(row=11,sticky=W)
Button(ventana, text="Ver", command=seleccionar).grid(row=12, sticky=W)
ventana.mainloop()