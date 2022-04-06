name = "Sergio Hernández"

# returns the data type
print (type(name))

# Detects the data type
comprobar = isinstance(name, str)

# Clean spaces before and after text, but not between text
frase ="  Hello World  "
print(frase.strip())

#clear variables
year = 2021
del year 
# print(year)

# returns the value of the string
# Countcharacter Count
text = "Hello"
if len (text) <=0:
    print("The variable is empty")

else:
    print(len(text))


# Busca un caracter, lo regresa como entero
# Find character, returs an integer value
frase = "Life is Beautiful"
print (frase.find("is"))

#Remplazar palabras en un string
#Replace words in a string

nueva_frase= frase.replace ("is", "is not")
print(nueva_frase)
print(frase.replace("is","sí es"))

# Mayusculas y Minusculas

print(name)
#mayusculas
print(name.upper())
#minusculas
print (name.lower())




