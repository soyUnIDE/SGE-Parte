# La función cargar devuelve una lista con 10 elementos numericos
def cargar():
    lista=[]
    for i in range(10):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista

# La función generar listas devuelve dos listas una con los valores positivos y otra con los valores negativos de la lista que se pasa como parametro
def generar_listas(lista):
    listaNeg=[]
    listaPos=[]
    for i in range(len(lista)):
        if lista[i]<0:
            listaNeg.append(lista[i])
        elif lista[i]>0:
            listaPos.append(lista[i])
    return [listaNeg,listaPos]

# La función imprimir imprime cada valor de la lista que se le pasa como parametro
def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i])

lista=cargar()
listaNeg,listaPos=generar_listas(lista)
print("Lista con los valores negativos.")
imprimir(listaNeg)
print("Lista con los valores positivos.")
imprimir(listaPos)