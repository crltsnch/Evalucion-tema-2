try:
    numero = 7/0
except ZeroDivisionError:
    print("No se puede dividir entre 0")

try:
    lista = [4, 7, 30, 23, 5]
    lista[10]
except IndexError:
    print("Ese número no está en la lista")

try:
    paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
    paises["alemania"]
except KeyError:
    print("Ese pais no está en el diccionario")

try:
    resultado = "2" + 10
except TypeError:
    print("No se puede sumar texto y un número")