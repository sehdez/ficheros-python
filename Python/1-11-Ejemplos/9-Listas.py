"""
LISTAS (arrays)
Son una colección de datos bajo un mismo nombre.
para acceder a esos valores podemos usar un índice numérico

"""

array = [1,2,3,4,5]
#es lo mismo pero en forma de lista
array2 = list((1,2,3,4,5))
arregloConRango = list(range(2020,2050))
#variada =["victor", 4, true]

print(array2[1:5])
#print(arregloConRango)
print("\n")


# Agregar Elemento a la lista

nombres=["Sergio", "Chutas", "Briss"]
"""
cantidad = int(input("Ingresa la cantidad de nombres que vas a agregar a la lista: "))
for i in range(cantidad):
    nombres.append(input((f"Ingresa el nombre #{i+1}: ")))

for i in range(cantidad):
    print(nombres[i])

#Versión sencilla
for i in nombres:
    print (i)

#Con Índice
for i in nombres:
    print(f"{nombres.index(i)+1}.- {i}")

"""
"""
#Ejercicio

lista =[] 
nuevaLista = ""

while nuevaLista!= "salir" :
    nuevaLista = input()
    lista.append(nuevaLista)
"""

#Contactos arreglos bidimencionales

contactos = [
    [
        "Juan",
        "Hernández"
    ],
    [
        "Sergio",
        "Chavez"
    ]

]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else: 
            print (f"Apellido: {elemento}")
    print()



