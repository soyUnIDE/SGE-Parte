# La clase Alumnos la cual almacena una lista de nombres y de notas
class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    # La funcion menu de la clase Alumnos muestra unas opciones por pantall y segun cual sea hace una funcion o otra
    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()

    # La funcion cargar de la clase Alumnos pide al usuario un nombre y una nota y las almacena en las listas y repite lo repite 5 veces
    def cargar(self):
        for x in range(5):
            nom=input("Ingrese nombre del alumno:")
            self.nombres.append(nom)
            no=int(input("Nota del alumno:"))
            self.notas.append(no)

    # La funcion listar de la clase Alumnos muestra por pantalla los valores de las listas de la clase
    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print(self.nombres[x],self.notas[x])
        print("_____________________")            

    # La funcion notas_altas de la clase Alumnos muestra por pantalla los valores de las listas de la clase si su nota es mayor o igual a 7
    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(5):
            if self.notas[x]>=7:
                print(self.nombres[x],self.notas[x])
        print("_____________________")                


# bloque principal

alumnos=Alumnos()
alumnos.menu()