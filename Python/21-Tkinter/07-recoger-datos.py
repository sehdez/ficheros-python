from tkinter import *
ventana = Tk()

def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        entrada.config(bg="yellow")
    else:
        entrada.config(bg="white")
dato = StringVar()
resultado = StringVar()



ventana.geometry("700x500")
Label(ventana).grid(row=0, column=0)
Label(ventana, text="Ingresa un texto:").grid(row = 0, column= 1, sticky=W)
Entry(ventana, textvariable=dato).grid(row = 0, column= 2, sticky= W)

Label(ventana, text="Dato: ").grid(row=1, column=1,sticky= W)
entrada = Entry(ventana, textvariable=resultado)
entrada.grid(row = 1, column= 2, sticky= W)
#entrada.config(state="disable")
Button(ventana, text="Accionar", command=getDato).grid(row=2, column=2)






ventana.mainloop()