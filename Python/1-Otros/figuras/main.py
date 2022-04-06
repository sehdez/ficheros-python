import figuras
largo = int(input("Ingresa el largo de las figuras: "))
car = input("Ingresa un sólo caracter para dibujar las figuras: ")
if largo%2 == 0:
    largo +=1
if largo> 79:
    largo = 79
media = int (largo / 2)

figuras = figuras.figuras(media,largo,car)

print(figuras.figuraA())
print (figuras.figuraB())
print(figuras.figuraAB())