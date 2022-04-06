"""
Crear un programa que tenga:
    - Ventana
    - Tamaño Fijo
    - No redimensionable
    - Un menú (Inicio, Añadir, Información, Salir)
    - Diferentes pantallas
    - Guardar datos temporalmente
    - Mostrar datos listados en la pantalla home 
    - Opcion de salir
"""

from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk

# Definir Ventana
ventana = Tk()
#ventana.geometry("400x400")
ventana.title("Proyecto Tkinter | By Sergio Hernández")
ventana.resizable(0,0)
ventana.minsize(400,400)


def add_product():
    if len(name_data.get())> 0 and len(price_data.get())>0 and len(add_description_entry.get("1.0","end-1c"))>0:
        products.append([
            name_data.get(),
            price_data.get(),
            add_description_entry.get("1.0","end-1c")
        ])
        name_data.set("")
        price_data.set("")
        add_description_entry.delete("1.0",END)
        MessageBox.showinfo("Éxito", "Los datos se guardaron con éxito.")
        inicio()
    else:
        MessageBox.showerror("Error", "Tiene que llenar todos los campos.")
    
        



# Definir Variables importantes
products=[]
name_data = StringVar()
price_data = StringVar()
descripcion_data = StringVar()





# Ventanas

products_box = Frame(ventana, width=250)
home_label = Label(products_box,text="Inicio")

Label(products_box).grid(row=1)
products_table = ttk.Treeview(height=12, columns=2)


info_label = Label(ventana,text="Información")


def inicio():
    
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 15),
        padx=20,
        pady=20,
        width= 33
    )
    products_box.grid(row=0)
    home_label.grid(row=0, column=0, sticky=N)

    products_table.grid(row=2, column=0, columnspan=2)
    products_table.heading("#0",text="Producto", anchor=W)
    products_table.heading("#1",text="Precio", anchor=W)



    # Listar productos
    """
    for product in products:
        if len(product)==3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="-----------------").grid()
    """
    for product in products:
        if len(product)==3:
            product.append("added")
            products_table.insert("", 0, text=product[0], values=product[1])

    # Ocultar pantallas
    info_label.grid_remove()
    add_frame.grid_remove()
    


    

def agregar ():
    # Encabezado    

    # Mostrar Pantalla
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 15),
        padx=20,
        pady=20,
        width= 33
    )
    add_label.grid(row=0, column=0,columnspan= 10, sticky=N)

    # Campos del formulario
    add_frame.grid(row=0)
    add_name_label.grid(row=1, column=0, pady=5, padx=5, sticky= E)
    add_name_entry.grid(row=1, column=1, pady=5, padx=5, sticky= W)

    add_price_label.grid(row=2, column=0, pady=5, padx=5, sticky= E)
    add_price_entry.grid(row=2, column=1, pady=5, padx=5, sticky= W)

    add_description_label.grid(row=3, column=0, pady=5, padx=5, sticky= NE)
    add_description_entry.grid(row=3, column=1, pady=5, padx=5, sticky= W)
    add_description_entry.config(width=25, height=5, font=("Arial",11), padx=5, pady=5)

    boton.grid(row=4, column= 1, sticky=NW,pady=5, padx=5,)
    boton.config(pady=3, bg="black", fg="white")

    # Ocultar Pantallas
    products_box.grid_remove()
    info_label.grid_remove()
    products_table.grid_remove()

def informacion():
    
    info_label.config(
        font=("Arial", 15),
        fg="white",
        bg="black",
        padx=20,
        pady=20,
        width= 33
    )
    info_label.grid(row=0, column=0,columnspan= 10, sticky=N)
    # Ocultar pantallas
    products_box.grid_remove()
    add_frame.grid_remove()
    products_table.grid_remove()
    


# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=inicio)
menu_superior.add_command(label="Añadir", command=agregar)
menu_superior.add_command(label="Información",command=informacion)
menu_superior.add_command(label="Salir", command= ventana.quit)

# Inicio

# Agregar
# Campos del formulario
add_frame = Frame(ventana)
add_label = Label(add_frame,text="Añadir Producto")

add_name_label= Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable= name_data)

add_price_label= Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable= price_data)

add_description_label= Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame)

boton= Button(add_frame, text="Guardar", command= add_product)



# Información


# Cargar pantalla Inicio
inicio()




# Cargar menú
ventana.config(menu= menu_superior)

# Cargar Ventana
ventana.mainloop()