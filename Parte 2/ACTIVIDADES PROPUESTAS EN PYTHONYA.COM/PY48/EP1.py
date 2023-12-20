# La Clase Jugador en la cual hay un tiempo definido y se guarda el nombre y el puntage
class Jugador:
    tiempo=30

    def __init__(self,nombre,puntaje):
        self.nombre=nombre
        self.puntaje=puntaje
    # La funcion imprimir de la clase Jugador imprime el nombre, el puntaje y lo que queda de tiempo
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puntaje: {self.puntaje}")
        print(f"Fin de juego en {self.tiempo} minutos")

    # La funcion pasar_minutos de la clase Jugador resta 1 el valor del tiempo
    def pasar_minutos(self):
        Jugador.tiempo-=1


jugador1=Jugador("Ana",100)
jugador2=Jugador("Juan",50)
while Jugador.tiempo>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_minutos()