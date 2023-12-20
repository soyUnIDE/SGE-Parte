# La clase Alumno que guarda un nombre y una nota
class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    # La funcion imprimir de la clase Alumno imprime por pantalla el nombre y la nota del alimno
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    # La funcion mostrar_estado de la clase Alumno imprime por pantalla la palabra Regular si la nota es mayor o igual a 4 o Libre si es menor
    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()