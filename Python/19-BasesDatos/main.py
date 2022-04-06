import mysql.connector

# Conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "ChinoMaster"
)

#Cursor para permitir consultas
cursor = database.cursor(buffered = True)


"""
#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS ChinoMaster")

#Mostrar bases de datos
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print (bd)
"""

# Crear Tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar (40) not null,
precio float (10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")

"""# Mostrar tabla
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)"""

# Agregar Valores
#cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', '18500')")
#database.commit()


"""# Agregar multiples valores
coches = [
    ('Seat','Ibiza',5000),
    ('Lamborguini','Gallardo',15000),
    ('Koenigsegg','Regadera',85000),
    ('Nissan','Tsuru',1000)

]
cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",coches)
database.commit()

"""
# Hacer consultas con condiciones
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Nissan'")
result = cursor. fetchall() # fetchone() es para sacar el primer dato de la tabla
print(result)

for coche in result:
    print(coche[1], coche[2])

# Borrar campos
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Seat'")
database.commit()

# Mostrar el numero de elementos eliminados
print (cursor.rowcount, " registros borrados")



# Acuatlizar datos
cursor.execute ("UPDATE vehiculos SET precio = '2000' WHERE marca = 'Nissan' ")
database.commit()
print (cursor.rowcount, " registros actualizados")



