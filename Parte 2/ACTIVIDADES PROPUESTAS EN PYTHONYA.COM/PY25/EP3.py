# La funcion retornar_superficie recibe dos valores numericos como parametro y retorna el resultado de la pultiplicación de los mismos
def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie

print("Primer rectangulo")
lado1=int(input("Ingrese lado menor del rectangulo: "))
lado2=int(input("Ingrese lado mayor del rectangulo: "))

print("Segundo rectangulo")
lado3=int(input("Ingrese lado menor del rectangulo: "))
lado4=int(input("Ingrese lado mayor del rectangulo: "))

# Según que superficie se mayor o si son iguales te lo notifica
if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("Los dos rectangulos tienen la misma superficie.")
elif retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
    print("El primer rectangulo tiene mayor superficie.")
else:
    print("El segundo rectangulo tiene mayor superficie.")