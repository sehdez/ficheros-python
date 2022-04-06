class figuras:
    def __init__(self,media, largo, car):
        self.media = media
        self.largo = largo
        self.car = car
    
    def figuraA(self):
        print("\n\tFigura A\n")
        cadena =""
        for i in range (self.largo):
            for j in range(self.largo):
                if i == 0 or i == self.largo-1 or j == 0 or j== self.largo-1:
                    cadena += f"{self.car}  "
                else:
                    cadena += "   "
            cadena += "\n"
        return cadena

    def figuraB(self):
        print("\n\tFigura B\n")
        cadena =""
        for i in range(self.largo):
            for j in range(self.largo):
                if j == 0+i or j == self.largo-1 - i or j == self.media or i == self.media:
                    cadena += f"{self.car}  "
                else:
                    cadena += "   "
            cadena += "\n"
        return cadena


    def figuraAB(self):
        print("\n\tFigura AB\n")
        cadena =""
        for i in range(self.largo):
            for j in range(self.largo):
                if i==0 or i == self.largo -1 or j== 0 or j== self.largo-1 or i == self.media or j== self.media or j == 0+i or j+1== self.largo-i:
                    cadena += f"{self.car}  "
                else:
                    cadena += "   " 
            cadena +="\n"
        return cadena






            



