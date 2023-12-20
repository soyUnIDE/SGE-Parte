# La clase Socio se guarda un valor tipo cadena y otro tipo numerico
class Socio:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del socio: ")
        self.antiguedad=input("Ingrese la antiguedad: ")

    # La funcion imprimir de la clase Socio muestra por pantalla el socio
    def imprimir(self):
        print(f"{self.nombre} tiene una antiguedad de {self.antiguedad}")

    # La funcion retornar_antiguedad de la clase Socio devuelve la antiguedad del socio
    def retornar_antiguedad(self):
        return self.antiguedad

# La clase Club se guarda tres valores de tipo Socio
class Club():

    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()

    # La funcion mayor_antiguedad de la clase Club muestra por pantalla el socio con mayor antiguedad
    def mayor_antiguedad(self):
        print("Socio con mayor antiguedad")
        if self.socio1.retornar_antiguedad()>self.socio2.retornar_antiguedad() and self.socio1.retornar_antiguedad()>self.socio3.retornar_antiguedad():
            self.socio1.imprimir()
        elif self.socio2.retornar_antiguedad()>self.socio3.retornar_antiguedad():
            self.socio2.imprimir()
        else:
            self.socio3.imprimir()

club=Club()
club.mayor_antiguedad