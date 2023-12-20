# La funcion cargar crea una lista de contactos, la cual como identificador tiene el nombre y como valor el telefono y lo repite hasta que el usuario quiera y devuelve toda la lista
def cargar():
    contactos={}
    continua="s"
    while continua=="s":
        nombre=input("Ingrese el nombre del contacto:")
        telefono=input("Ingrese el numero de telefono:")
        contactos[nombre]=telefono
        continua=input("Ingresa otro contacto[s/n]?:")
    return contactos

# La funcion modificar_telefono recibe una lista como parametro y si existe el nombre preguntado pregunta por el nuevo numero y si no notifica de que no existe el nombre en la lista
def modificar_telefono(contactos):
    nombre=input("Ingrese el nombre de contacto a modificar el telefono:")
    if nombre in contactos:
        telefono=input("Ingrese el nuevo numero telefonico")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado")

# La funcion modificar_telefono recibe una lista como parametro y si existe el nombre preguntado pregunta por el nuevo numero y si no notifica de que no existe el nombre en la lista
def imprimir(contactos):
    print("Listado de todos los contactos")
    for nombre in contactos:
        print(nombre,contactos[nombre])


# bloque principal

contactos=cargar()
imprimir(contactos)
modificar_telefono(contactos)
imprimir(contactos)