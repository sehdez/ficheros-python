#Importar el modulo para sqlite
import sqlite3

# Conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()



# crear una tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int (255)
    );
""")

# Guardar Cambios
conexion.commit()

# Insertar Datos
#cursor.execute("INSERT INTO productos VALUES (null, 'Segundo Producto', 'Descripción del producto', 550)")
#conexion.commit()

# Listar Datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall() # fetchone() para mostrar el primer registro


#Eliminar datos
#cursor.execute("DELETE FROM productos")
#conexion.commit()

"""for producto in  productos:
    print(f"Nombre: {producto[1]}")"""

#Insertar muchos registros de golpe
"""productos =[
    ("Ordenador portatil", "Buen ordenador", 700),
    ("Ordenador movil", "Buen celular", 300),
    ("tablet", "Buena tablet", 700),
    ("X BOX ONE S", "Excelente consola", 700)
] 
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit()
"""
# Actualizar datos 
cursor.execute("UPDATE productos SET precio = 550 WHERE precio =700")


cursor.execute("SELECT * FROM productos ")
productos = cursor.fetchall()
conexion.commit()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")





# Cerrar conexión 
conexion.close()




