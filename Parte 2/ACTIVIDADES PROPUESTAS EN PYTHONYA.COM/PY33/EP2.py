# Funcion cargar crea una lista de 5 elementos con otra lista dentro donde contiene un valor de tipo cadena y otro de tipo numerico y devuelve la lista
def cargar():
    productos=[]
    for i in range(5):
        nombre= input("Ingrese el nombre del producto: ")
        precio= int(input("Ingrese el precio: "))
        productos.append((nombre,precio))
    return productos

# Funcion imprimir imprime por pantalla el nombre y el precio de los productos
def imprimir(productos):
    print("Listado de los productos y sus precios")
    for nombre,precio in productos:
        print(nombre,precio)

# Funcion imprimir imprime por pantalla el nombre y el precio de los productos si el precio de los productos está entre 10 y 15
def imprimir_entre10y15(productos):
    print("Listado de los productos que tienen un precio comprendido entre 10 y 15")
    for nombre,precio in productos:
        if precio>=10 and precio<=15:
            print(nombre,precio)


productos=cargar()
imprimir(productos)
imprimir_entre10y15(productos)