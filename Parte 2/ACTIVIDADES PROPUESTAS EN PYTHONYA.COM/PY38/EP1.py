# La funcion cargar crea una lista con 5 valores de tipo string y la devuelve
def cargar():
    palabras=[]
    for i in range(5):
        pal=input("Ingrese una palabra: ")
        palabras.append(pal)
    return palabras

# La funcion intercambiar cambia el orden del primer elemento y el ultimo
def intercambiar(palabras):
    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux

# La funcion imprimir muestra por pantalla lo que le pase por parametro
def imprimir(palabras):
    print(palabras)

palabras=cargar()
imprimir(palabras)
intercambiar(palabras)
imprimir(palabras)