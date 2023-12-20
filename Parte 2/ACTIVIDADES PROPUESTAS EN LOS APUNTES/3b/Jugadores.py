class Jugador:
    def __init__(self,d,n):
        self.dorsal=d
        self.nombre=n

    def mostrar(self):
        print(self.dorsal,self.nombre)

jugador=Jugador(16,"Pau Gasol")
jugador.mostrar()