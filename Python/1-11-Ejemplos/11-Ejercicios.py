"""
Ejercicio 1:
    Hacer una lista que tenga 8 números enteros...
    1: recorrerla y mostrarla
    1.2: Hacer una función que recorra listas de números y devuelva un string
    2: ordenarla y mostrarla
    3: mostrar su longitud
    4: buscar algún elemento que el usuario pida

"""
# FUNCIÓN PARA RECORRER LISTAS
def recorrerListas(lista):
    cadena = ""
    for i in lista:
        cadena =cadena + "Elemento #" + str(lista.index(i)+1) + " " + str(i) + " \n"
    return cadena

#lista
numeros = [30,60,40,10,20,80,70,50]

for numero in numeros:
    print(numero)

# Ordenar lista
numeros.sort()

print(recorrerListas(numeros))

print(f"La lista tiene {len(numeros)} elementos")

"""Ejercicio 2:
    validar si una variable está vacía,
    de ser así, rellenarla con texto en minuscula
    y mostrarla en mayusculas.
"""
texto = " "

if len(texto.strip()) <= 0:
    texto = "texto en minúsculas"
    print (texto.upper())

else: 
    print("La variable tiene texto")

"""
Crear una lista con el contenido de esta tabla:

ACCION:             AVENTURA                DEPORTES

GTA                 ASSASSINS                FIFA 21
COD                 CRASH                   PRO 21
PUGB                PRINCE OF PERSIA        MOTO GP 21


"""
print("\n*******Ultimo Ejercicio*******")


videojuegos= [
    {
        "categoria": "ACCION",
        "juegos" : ["GTA", "COD","PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos" : ["ASSASIN'S CREED", "CRASH","PRINCE OF PERSIA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos" : ["FIFA 2021", "PRO EVOLUTION SOCCER 2021","MOTO GP 2021"]
    }

]


for categoria in videojuegos:
    print(f"----------{categoria['categoria']}----------")
    for elementos in categoria['juegos']:
        print(elementos)