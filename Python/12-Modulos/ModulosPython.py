import datetime

print (datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada  = fecha_completa.strftime("%d/%m/%Y %H:%M:%S")
print(fecha_personalizada)



# MODULO MATEMÁTICAS
import math
print("Raíz cuadrada de 10 es: ", math.sqrt(10))

# Modulo Random
import random

print("El numero aleatorio entre 1 y 100 es: ", random.randint(1,100))




