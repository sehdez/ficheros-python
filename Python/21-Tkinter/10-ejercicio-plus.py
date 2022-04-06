"""
    Calculadora:
        Dos campos de texto
        4 botones para las operaciones
        mostrar el resultado en una alerta

"""
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title("Mini calculadora")
ventana.geometry("300x300")


class Calculadora:
    valor1 = StringVar()
    valor2 = StringVar()
    resultado = StringVar()

    def error(self):
        MessageBox.showerror("Datos incorrectos", "Error en los campos")
        self.valor1.set("")
        self.valor2.set("")
        self.resultado.set("")



    def suma(self):
        try:
            self.resultado.set(float(valor1.get()) + float (valor2.get()))
            self.mostrarResultado()
        except:
            self.error()
    def resta(self):
        try:
            self.resultado.set(float(valor1.get()) - float (valor2.get()))
            self.mostrarResultado()
        except:
            self.error()
    def mult(self):
        try:
            self.resultado.set(float(valor1.get()) * float (valor2.get()))
            mostrarResultado()
        except:
            error()
    def div(self):
        try:
            resultado.set(float(valor1.get()) / float (valor2.get()))
            mostrarResultado()
        except:
            error()
    def mostrarResultado(self):
        MessageBox.showinfo("Resultado", f"El resultado es: {resultado.get()}")
        valor1.set("")
        valor2.set("")
        resultado.set("")




    
    labelValor1 = Label(ventana, text="Valor 1:")
    labelValor1.place(x=10, y=10)
    txtValor1 = Entry(ventana, textvariable= valor1).place(x=70, y=10)

    labelValor2 = Label(ventana, text="Valor 2:")
    labelValor2.place(x=10, y=40)
    txtValor2 = Entry(ventana, textvariable= valor2).place(x=70, y=40)

    labelResult = Label(ventana, text="Resultado:")
    labelResult.place(x=10, y=70)
    txtResult = Entry(ventana,state="readonly", textvariable=resultado)
    txtResult.place(x=70, y=70)

    


    bSuma= Button(ventana, text = "+", command = lambda: suma()).place(x=70,y=100)
    bResta= Button(ventana, text = "-", command = lambda: resta()).place(x=100,y=100)
    bMult= Button(ventana, text = "*", command = lambda: mult()).place(x=130,y=100)
    bDiv= Button(ventana, text = "/", command = lambda: div()).place(x=160,y=100)



    ventana.mainloop()
