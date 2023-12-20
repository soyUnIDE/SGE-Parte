class Equipo:

    def __init__(self,n):
        self.nombre=n

    def mostrar(self):
        return self.nombre

class Jugador:

    def __init__(self,d,n,e):
        self.dorsal=d
        self.nombre=n
        self.equipo=e

    def mostrar(self):
        print("Dorsal:",self.dorsal,",Nombre:",self.nombre,",Nombre del equipo:",self.equipo.mostrar())



equipo=Equipo("Los Angeles Lakers")
jugador=Jugador(16,"Pau Gasol",equipo)
jugador.mostrar()