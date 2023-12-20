# Importamos el modulo ramdom
import random

# La clase Dado la cual almacena un valor random entre el 1 y el 6
class Dado:

    def tirar(self):
        self.valor=random.randint(1,6)

    # La funcion imprimir de la clase Dado imprime el valor del dado
    def imprimir(self):
        print("Valor del dado:",self.valor)

    # La funcion retornar_valor de la clase Dado devuelve el valor del dado
    def retornar_valor(self):
        return self.valor

# La clase JuegoDeDados la cual almacena 3 variables de tipo Dado
class JuegoDeDados:

    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    # La funcion jugar de la clase JuegoDeDados imprime por pantalla si ganas o pierdes y ganas si el valor de todos los lados es el mismo
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
            print("Gano")
        else:
            print("Perdio")


# bloque principal del programa

juego_dados=JuegoDeDados()
juego_dados.jugar()