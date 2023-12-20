# La funcion cargar llena una lista de personas con 4 elementos en el que el identificador es el numero introducido y el valor es el nombre
def cargar():
    personas={}
    for i in range(4):
        numero=int(input("Ingrese el numero de documento: "))
        nombre=input("Ingrese el nombre de la persona: ")
        personas[numero]=nombre
    return personas

# La funcion imprimir imprime las personas con su identificador y nombre
def imprimir(personas):
    print("Listado completo del diccionario")
    for numero in personas:
        print(numero,personas[numero])

# La funcion consulta_por_numero consulta si existe el identificador preguntado y si existe muestra el nombre y si no existe se avisa de que no exite
def consulta_por_numero(personas):
    nro=int(input("Ingrese el numero de documento a consultar: "))
    if nro in personas:
        print(f"Nombre de la persona {personas[nro]}")
    else:
        print("No existe persona con dicho numero de documento.")

personas=cargar()
imprimir(personas)
consulta_por_numero(personas)