from os import system
from Usuarios import acciones
hazEl = acciones.Acciones()
opcion = 1
while opcion != "3":
    opcion = hazEl.menu()
    if opcion == "1":
        hazEl.login()
    elif opcion == "2":
        hazEl.registro()
