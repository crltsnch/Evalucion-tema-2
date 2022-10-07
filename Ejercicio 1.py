class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
    def nota(self):
        if self.nota>=5:
            print("Ha aprobado")
        else:
            print("Ha suspendido")

Nombre = input("Escribe el nombre del alumno: ")
Nota = input("Escriba la nota del alumno: ")

Alumno1 = Alumno('nombre', 'nota')
Alumno1.imprimir()