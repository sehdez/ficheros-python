"""
Modulos: Son Funcionalidades ya hechas para reutilizar

"""
#Para importar todo el módulo
import MiModulo


# Para importar todas las funcionens del modulo
from MiModulo import *

# Aquí sólo importamos una función en especifico
from MiModulo import saludo


# Para llamar a la función cuando importas todo el módulo
print(MiModulo.saludo("Chino"))

# Para llamar a la función especifica del módulo
print(saludo("Sergio"))





