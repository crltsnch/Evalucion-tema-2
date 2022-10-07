class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
    def imprimir(self):
        print("Código: ", self.codigo)
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)
        print("Tipo: ", self.tipo)
    def __str__(self):
        return (self.codigo + self.nombre + self.precio + self.tipo)
    
Producto1 = (336, "Caja", 5, "Organización")
print(Producto1)

Producto2 = (287, "Cuadro", 22, )