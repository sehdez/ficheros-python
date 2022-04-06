from coche import Coche

carro = Coche("Amarrillo", "Lamborguini", "Murciélago", 300, 600, 4)
carro2 = Coche("Verde", "Ford", "Fiesta", 300, 600, 4)
carro3 = Coche("Blanco", "Kia", "Riu", 300, 600, 4)
carro4 = Coche("Azul", "Toyota", "Corolla", 300, 600, 4)



print(carro.getInformacion())
print(carro2.getInformacion())
print(carro3.getInformacion())
print(carro4.getInformacion())
 
carro3 = "Aleatorio"
# Detectar Tipado
if type (carro3) == Coche:
    print ("Es un objeto correcto")
else:
    print("No es un objeto")

# Visibilidad
# Acceder a un atributo privado
carro.setPrivado(input("Ingresa texto: "))
print("El texto privado es: "+carro.getPrivado())




