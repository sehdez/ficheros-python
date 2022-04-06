"""
#FOR

for variable in elemento_iterable (lista,rango, etc)
    BLOQUE DE INSTRUCCIONES

"""


"""
contador = 0
resultado = 0


for contador in range(0,5):
    print ("Voy por el " + str(contador))
    resultado += contador

print (f"El resultado es: {resultado}")

#EJEMPLO 2 TABLA DE MULTIPLICAR

print ("\n################# EJEMPLO 2 #####################")
numeroUsuario = int (input("¿De qué número quieres la tabla?: "))
numeroTope = int(input("Hasta que número quieres que se ejecute la table?: "))
contador = 1

for contador in range(1,numeroTope+1):
    print(f"{numeroUsuario} * {contador} = {numeroUsuario * contador}")

print(contador)
"""


"""
while condicion:
    bloque de instrucciones
    actualizacion de condicion
"""
"""
contador = 1
muestrame = str(0)
while contador <=20:
    print (contador)
    muestrame = muestrame + "," + str(contador) 
    contador +=1
print (muestrame)

"""

numU= int (input("Ingresa un numero: "))
if numU < 1:
    numU = 1
contador = 1
while contador <=10:
    print(f"{numU} * {contador} = {numU*contador}")
    contador +=1
print("Tabla terminada")


