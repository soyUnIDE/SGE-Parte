# La clase Operacion guarda tres variables con valor a 0
class Operacion:

    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0

    # La funcion cargar1 de la clase Operacion modifica el valor de la primera variable de la clase
    def cargar1(self):
        self.valor1=int(input("Ingrese primer valor:"))

    # La funcion cargar2 de la clase Operacion modifica el valor de la segunda variable de la clase
    def cargar2(self):
        self.valor2=int(input("Ingrese segundo valor:"))

    # La funcion mostrar_resultado de la clase Operacion muestra por pantalla el valor de la tercera variable
    def mostrar_resultado(self):
        print(self.resultado)

    # La funcion operar de la clase Operacion la definimos pero no le implementamos ninguna funcionalidad aun
    def operar(self):
        pass

# La clase Suma hereda de la clase Operacion y modifica la funcionalidad de la funcion operar para que la tercera variable sea el resultado de la suma de los dos anteriores
class Suma(Operacion):

    def operar(self):
        self.resultado=self.valor1+self.valor2

# La clase Resta hereda de la clase Operacion y modifica la funcionalidad de la funcion operar para que la tercera variable sea el resultado de la resta de los dos anteriores
class Resta(Operacion):

    def operar(self):
        self.resultado=self.valor1-self.valor2


# bloque princpipal

suma1=Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
print("La suma de los dos valores es")
suma1.mostrar_resultado()

resta1=Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
print("La resta de los valores es:")
resta1.mostrar_resultado()