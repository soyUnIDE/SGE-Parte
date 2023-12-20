# La clase Tringulo al crear un objeto pregunta al usuario por un valor numerico que sera un lado y lo repite 3 veces
class Triangulo:
    def __init__(self):
        self.lado1=int(input("Ingrese el primer lado: "))
        self.lado2=int(input("Ingrese el segundo lado: "))
        self.lado3=int(input("Ingrese el tercer lado: "))

    # La función imprimir de la clase Tringulo imprime los lados del triangulo
    def imprimir(self):
        print(f"Lado1: {self.lado1}")
        print(f"Lado2: {self.lado2}")
        print(f"Lado3: {self.lado3}")

    # La función lado_mayor de la clase Tringulo muestra por pantalla el lado de mayor longitud
    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        elif self.lado2>self.lado3:
            print(self.lado2)
        else:
            print(self.lado3)

    # La función es_equilatero de la clase Tringulo muestra por pantalla si el triangulo es equilatero
    def es_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triangulo es equilatero.")
        else:
            print("El triangulo no es equilatero.")

triangulo=Triangulo()
triangulo.imprimir()
triangulo.lado_mayor()
triangulo.es_equilatero()