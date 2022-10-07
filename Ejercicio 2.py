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

    def __str__(self):
        return(self.nombre + self.nota)

Alumno1 = ("Carla", 9)
print(Alumno1)

Alumno2 = ("Iván", 4)
print(Alumno2)
