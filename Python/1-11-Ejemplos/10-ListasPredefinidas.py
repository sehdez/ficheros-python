cantantes = ["Blink-182", "Sum 41", "Metallica","Strokes"]
numeros = [1,3,5,2,4,8,6,6,6,6,9]

#Ordenar Listas
numeros.sort()
print(numeros)

#Agregar elementos
cantantes.append("Green Day") # se agrega al final de la lista
cantantes.insert(1,"RHCP") # Se le asigna un valor para posicionarse
print(cantantes)



#Eliminar elementos
cantantes.pop (5) #Se eliminar por posicion
cantantes.remove("Sum 41")
print(cantantes)


# Dar la Vuelta a la lista

cantantes.reverse()
print(cantantes)
cantantes.reverse()
print(cantantes)



# Buscar dentro de una lista
print ("RHCP" in cantantes) #devuelve verdadero o falso



# Contar el numero de elementos
print (len(cantantes))


#Contar las veces que aparece un elemento
print (numeros.count(6))

#Buscar Indice de un elemento
print(cantantes.index("Metallica"))


# Unir dos listas
cantantes.extend(numeros)
print(cantantes)

