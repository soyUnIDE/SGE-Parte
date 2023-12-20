# La funcion cargar crea una lista con 10 valores numericos introducidos por el usuario y la devuelve
def cargar():
    lista=[]
    for i in range(10):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista

# La funcion retornar_mitad devuelve en una lista los valores desde el principio a la mitad de la lista que se le pasa como parametro
def retornar_mitad(lista):
    return lista[:len(lista)//2]

# La funcion imprimir imprime la lista que se le pasa como parametro
def imprimir(lista):
    print(f"Contenido de la lista\n{lista}")

lista=cargar()
lista2=retornar_mitad(lista)
imprimir(lista)
imprimir(lista2)