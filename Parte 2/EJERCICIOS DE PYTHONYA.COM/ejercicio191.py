# La clase punto la cual almacena dos variables x e y
class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    # La funcion imprimir de la clase Punto muestra por pantalla el valor de x y de y
    def imprimir(self):
        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    # La funcion imprimir_cuadrante de la clase Punto muestra por pantalla al nombre de la cuadrante segun si las variables son positivas o negativas
    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")


# bloque principal

punto1=Punto(10,-2)
punto1.imprimir()
punto1.imprimir_cuadrante()