"""
Ejercicio 1.
    - Crear variables uan "pais" y otro "continente"
    - Mostrar su valor por pantalla (Imprimir)
    - Poner un comentario diciento el tipo 

"""
"""
Ejercicio 2.
    -Escribir un script que nos muestre por pantalla todos
    los números pares del 1 al 120
"""

"""
for contador in range(1,121):
    if contador%2==0:
        print (contador)

"""

"""
Ejercicio 3.
    - Escribir un programa que muestre los cuadrados 
    de los 60 primeros números naturales. Resolverlo con for y while
"""
"""
print("Resuelto con For")
for contador in range(1,61):
    print(f"{contador}^2 = {contador*contador}")

print("Resuelto con While")
contador = 1
while contador <=60:
    print(f"{contador}^2 = {contador*contador}")
    contador +=1
"""
"""
Ejercicio 6.
    - Mostrar todas la tablas de multimplicar del 1 al 10.
    Mostrando el titulo de la tabla y luego las multiplicaciones
"""
"""

for contador1 in range(1,11):
    print(f"\nTabla de Multiplicar del #{contador1}")
    for contador in range (1,11):
        print(f"{contador1} * {contador} = {contador1 * contador}")
"""

numero = int (input ("Ingresa un numero: "))
porcent = int (input ("porcentaje: "))

input(f"El %{porcent} de {numero} es: {numero*(porcent/100)}")
