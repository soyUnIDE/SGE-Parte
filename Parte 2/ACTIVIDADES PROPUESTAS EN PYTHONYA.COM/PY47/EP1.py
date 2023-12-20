# La clase Cuenta guarda dos valores el titular y el monto
class Cuenta:

    def __init__(self,titular,monto):
        self.titular=titular
        self.monto=monto

    # La funcion imprimir de la clase Cuenta imprime los valores de la cuenta
    def imprimir(self):
        print(f"Titular: {self.titular}")
        print(f"Monto: {self.monto}")

# La clase CajaAhorro guarda los valores de Cuenta
class CajaAhorro(Cuenta):

    def __init_subclass__(self,titular,monto):
        super().__init__(titular,monto)

    # La funcion imprimir de la clase CajaAhorro imprime los valores de la cuenta con un mensage anterior
    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()

# La clase PlazoFijo guarda los valores de Cuenta, un plazo y un interes
class PlazoFijo(Cuenta):

    def __init__(self, titular, monto,plazo,intereses):
        super().__init__(titular, monto)
        self.plazo=plazo
        self.intereses=intereses

    # La funcion imprimir de la clase PlazoFijo imprime los valores de la cuenta con un mensage anterior y el plazo y el interes y la ganancia
    def imprimir(self):
        print("Cuenta plazo fijo")
        super().imprimir()
        print(f"Plazo en dias: {self.plazo}")
        print(f"Intereses: {self.intereses}")
        self.ganancia()

    # La funcion ganancia de la clase PlazoFijo calcula la ganancia y la muestra por pantalla
    def ganancia(self):
        gan=self.monto*self.intereses/100
        print(f"Monto de intereses: {gan}")

cajadeahorro=CajaAhorro("Juan",1300)
cajadeahorro.imprimir()

plazoFijo=PlazoFijo("Ana",1000,30,0.75)
plazoFijo.imprimir()