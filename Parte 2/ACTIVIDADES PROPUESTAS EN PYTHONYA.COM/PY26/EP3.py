# La función producto recibe una lista como parametro y retorna el resultado de la multimplicacion de todos los elementos
def producto(lista):
    prod=1
    for i in range(len(lista)):
        prod=prod*lista[i]
    return prod

lista=[10,20]
print(lista)
print(f"Multiplicación de todos sus elementos {producto(lista)}.")