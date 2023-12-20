class Operaciones:
    def __init__(self):
        self.valor1=int(input("Ingrese el primer valor: "))
        self.valor2=int(input("Ingrese el segundo valor: "))

    def suma(self):
        suma=self.valor1+self.valor2
        print(f"La suma es {suma}")

    def resta(self):
        resta=self.valor1-self.valor2
        print(f"La resta es {resta}")

    def multimplicacion(self):
        multimplicacion=self.valor1*self.valor2
        print(f"La multimplicacion es {multimplicacion}")

    def division(self):
        division=self.valor1/self.valor2
        print(f"La division es {division}")

operacion=Operaciones()
operacion.suma()
operacion.resta()
operacion.multimplicacion()
operacion.division()