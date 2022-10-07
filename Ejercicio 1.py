class Alumno:
    def iniciar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
    def calificacion(self):
        if self.nota>=5:
            print("Ha aprobado")
        else:
            print("Ha suspendido")


Alumno1 = Alumno()
Alumno1.iniciar("Carla", 3)
Alumno1.imprimir()
Alumno1.calificacion()

Alumno2 = Alumno()
Alumno2.iniciar("Ivan", 7)
Alumno2.imprimir()
Alumno2.calificacion()