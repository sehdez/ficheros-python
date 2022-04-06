# Herencia: posibilidad de compartir atributos y métodos de clases

class Persona:
    """nombre 
    apellidos
    altura
    edad"""
    
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos
    
    def getEdad(self):
        return self.edad

    def getAltura(self):
        return self.altura

    def setNombre(self, nombre):
        self.nombre= nombre
    
    def setApellidos(self, apellidos):
        self.apellidos= apellidos

    def setAltura(self, altura):
        self.altura= altura

    def setEdad(self, edad):
        self.edad =  edad

    def hablar(self):
        return "Estoy  hablando"    

    def caminar(self):
        return "Estoy Caminando"
    
    def dormir (self):
        return "Estoy duermiendo"

class Informatico (Persona):
    """
    lenguajes
    experiencia
    """
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes

    def Aprender(self, lenguajes):
        self.lenguajes= lenguajes
        return self.lenguajes
    
    def programar (self):
        return "Estoy ptrogramando"
    
    def repararPC(self):
        return "He reparado un ordenador"

    

class TecnicoRedes(Informatico):

    
    def __init__(self):
        #LLamar al constructor de la clase padre
        super().__init__()
        
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15





