class Coche:
    color = "rojo"
    marca="Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    __privado = "Hola mundo"

    # Método constructor, es exclusivo para cada clase
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas) :
        self.color = color
        self.marca= marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    # Métodos, son acciones que hace el objeto (funciones)
    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -=1

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def getInformacion(self):
        info = "---- Información del coche------"
        info += "\n"+ self.getColor()
        info += "\n"+ self.getMarca()
        info += "\n"+ self.getModelo()
        info += "\n"+ str(self.getVelocidad()) + " Km/h"
        return info

    def setPrivado (self, texto):
        self.__privado = texto
    def getPrivado(self):
        return self.__privado
