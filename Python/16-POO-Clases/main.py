# Programación orientada a objetos (POO)
#Definir una clase (molde para crear más objetos de ese tipo
# (Coche) con caracteristicas similares)


class Coche:
    #Atributos o propiedades (variables)
    ##caracteristicas del coche
    color = "rojo"
    marca="Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

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


# Fin definición clase


# crear un objeto o instanciar la clase
coche = Coche()

coche.setColor("Negro")
coche.setMarca("Ford")
coche.setModelo("GT")
print("Coche 1")
print(coche.getColor(), coche.getMarca(), coche.getModelo(), coche.getVelocidad())


# Crear más objetos

coche2 = Coche()
print("-----Coche 2------")
print(coche2.getColor(), coche2.getMarca(), coche2.getModelo(), coche2.getVelocidad())
