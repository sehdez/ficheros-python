"""
numero = int(input("Ingresa un numero: "))
if color == 4:
    print(f"El numero es {color}")
else:
    print("El numero no es 4")
"""

nombre = "Sergio"
ciudad = "Barcelona"
continente = "Europa"
edad = 27
mayoriaEdad =  int(input("Ingresa tu edad: "))

if edad >= mayoriaEdad:
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print ("El usuario no es Europeo")
    else:
        print(f"Es Europeo y de la Ciudad de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

#elif