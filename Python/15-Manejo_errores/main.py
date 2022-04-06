# CAPTURAR ERRORES Y MANEJAR ERRORES EN CÓDIGO SUCEPTIBLE A FALLAS

#4nombre = input("¿Cuál es tu nombre? ")
"""try:
    if len(nombre) >= 3:
        nombreValidado = nombre
    
    print(f"Bienvenido {nombreValidado}")
except:
    print("El nombre debe tener al menos 3 caracteres")

# Multiples excepciones
try:
        
    numero = int(input("Ingresa un numero para elevarlo al cuadrado: "))
    print(f"{numero}^2 = {numero*numero}")
# Para un error en específico
except ValueError:
   print("Ingresaste un dato que no es numérico")

except Exception as e:
    print(f"Se ha generado el siguiente error: {type(e).__name__}")

"""

#Excepciones personalizadas
try:
    nombre= input("Nombre: ")
    edad = int (input("Edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es Real")
    elif len (nombre)< 3:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print(f"Se generó un error {e}")






