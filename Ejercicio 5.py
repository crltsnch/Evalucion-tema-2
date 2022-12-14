
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    tipo = ""
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Camion(Coche):
    carga = 0
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

class Motocicleta(Bicicleta):
    velocidad = 0
    cilindrada = 0
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

mo = Motocicleta("Roja", 2, "Triciclo", 120, 250)
ca = Camion("Blanco", 8, 90, 400, 400)
co = Coche("Negro", 4, 120, 600)
bi= Bicicleta("Rosa", 2, "Triciclo")
listaVehiculos = [mo.__dict__, ca.__dict__, co.__dict__, bi.__dict__]
print(listaVehiculos)

def catalogar(listaVehiculos, nRuedas = None):
    cuenta = 0
    for vehiculo in listaVehiculos:
        if nRuedas == vehiculo.ruedas:
            print(vehiculo)
            cuenta +=1
    if nRuedas:
        print("Se han encontrado {cuenta} vehiculos con {nRuedas ruedas}")