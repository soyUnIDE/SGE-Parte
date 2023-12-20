# La funcion cargar crea una lista de empleados que llena segun cuantas veces el usuario introduzca si en continua y crea un nuevo empleado con el identificador legajo en nombre del mismo, la profesion y el sueldo
def cargar():
    empleados={}
    continua="s"
    while continua=="s":
        legajo=int(input("Ingrese el numero de legajo: "))
        nombre=input("Nombre del empleado: ")
        profesion=input("Ingrese profesion: ")
        sueldo=float(input("Ingrese el sueldo: "))
        empleados[legajo]=[nombre,profesion,sueldo]
        continua=input("Ingresa los datos de otro empleado [s/n]: ")
    return empleados

# La funcion imprimir imprime la informacion de los empleados
def imprimir(empleados):
    print("Listado completo de los empleados")
    for legajo in empleados:
        print(legajo,empleados[legajo][0],empleados[legajo][1],empleados[legajo][2])

# La funcion modificar_sueldo busca primero el legajo del empleado y si lo encuentra le pregunta el nuevo sueldo y lo cambia
def modificar_sueldo(empleados):
    legajo=int(input("Ingrese el numero de legajo: "))
    if legajo in empleados:
        sueldo=float(input("Ingrese nuevo sueldo: "))
        empleados[legajo][2]=sueldo
    else:
        print("No existe un empleado con dicho numero de legajo")

# La funcion imprimir_analistas muestra la información de los empleados que tengan como profesion "analista de sistemas"
def imprimir_analistas(empleados):
    print("Listado de empleados con profesion \"Analista de sistemas\"")
    for legajo in empleados:
        if empleados[legajo][1].lower()=="analista de sistemas":
            print(legajo,empleados[legajo][0],empleados[legajo][2])

empleados=cargar()
imprimir(empleados)
modificar_sueldo(empleados)
imprimir(empleados)
imprimir_analistas(empleados)