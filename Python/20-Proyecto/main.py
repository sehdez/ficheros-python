"""
Proyecto Python MYSQL
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la DB
- Si elegimos Login, identificará al usuario y nos preguntara
- Crear, mostrar o borrar notas
"""
from Usuarios import acciones

hazEl = acciones.Acciones()


accion = hazEl.menu()

if accion == "1":
    hazEl.registro()

elif accion=="2":
    hazEl.login()
    


else:
    print("Tu selección no está en el menú")



"""
#31#

*#62#
"""
