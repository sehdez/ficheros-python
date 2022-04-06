import clases

persona = clases.Persona()

persona.setNombre("Sergio")
persona.setApellidos("Hernández")
persona.setAltura ("190 cm")
persona.setEdad (27)

print (f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print (persona.hablar())
print("--------------------------")

informatico = clases.Informatico()
informatico.setNombre("Chino")
informatico.setApellidos("Hernández")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(f"Y sabe {informatico.getLenguajes()}")