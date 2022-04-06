from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()

ventana.geometry("700x500")

# load image
imagen = Image.open("./Imagenes/java2.png")
render = ImageTk.PhotoImage(imagen)
Label(ventana,image = render).pack()



ventana.mainloop()