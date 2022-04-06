""" 
FUNCIONES: 
    Una funcion es un conjunto de instrucciones agrupadas
    bajo un mismo nombre concreto que pueden reutilizarse invocando
    a la funcion tantas veces sea necesario.

def nombreDeMiFuncion (parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion (mi_parametro)


"""
"""

# EJEMPLO 1

# Declarar Función
def mostrarNombres():
    print("Sergio")
    print("ALberto")
    print("Hernández")
    print("Cuevas")


# Invocar Función
mostrarNombres()
"""


"""
# EJEMPLO 2
def mostrarNombreParametro(n,e):
    print(f"Bienvenido {n}")    
    if e<18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")

    


nombre = input("Introduce tu nombre: ")
edad = int(input("Ingresa tu edad: "))

mostrarNombreParametro(nombre, edad)

"""

"""
# Ejemplo 3

def tabla(numero, opcional = 0):
    for contador in range (1,11):
        print(f"{numero} * {contador} = {numero*contador}")


#numero = int(input("Ingresa un número: "))

for contador in range(1,11):
    print(f"\nTabla del {contador}")
    tabla(contador)



# EJEMPLO 5 parametros opcionales y returns

def saludame(nombre):
    saludo = f"Bienvenido{nombre}"

    return saludo

print (saludame("Chinesse"))

"""

# FUNCION LAMBDA

dimeElAnio = lambda year: f"El año es {year}"

print(dimeElAnio(2015))


