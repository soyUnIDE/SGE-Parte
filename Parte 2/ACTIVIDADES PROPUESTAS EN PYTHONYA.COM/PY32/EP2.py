# Funcion carga_datos que devuelve lista y la llena de 3 valores con un valor de tipo cadena como primero y una lista como segundo parametro de longitud diferente que contiene una variable tipo cadena y otra de tipo numerica
def carga_datos():
    lista = []
    for i in range(3):

        nombre=input(("Ingrese el nombre del candidato : "))
        prov0=input("Ingrese la Provincia : ")
        votos_prov0=int(input("Ingrese los votos en esa Provincia : "))
        lista.append((nombre,[(prov0,votos_prov0)]))
    return lista

# Funcion impresion que imprime el nombre del candidato y los votos obtenidos
def impresion(lista):
    for i in range(3):
        print(f"Nombre candidato {lista[i][0]}")
        print(f"votos {lista[i][1][0][1]}")


lista=carga_datos()
impresion(lista)