# La clase Agenda se inicia con una lista vacia
class Agenda:
    def __init__(self):
        self.contactos={}

    # El metodo menu de la clase Agenda es un menu que se repite hasta que la opcion sea 5 y puedes cargar un nuevo contacto, listarlos, consultar por el nombre y modificar el contacto
    def menu(self):
        opcion=0
        while opcion!=5:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de una persona")
            print("4- Modificación del telefono y email")
            print("5- Finalizar el programa")
            opcion=int(input("Ingrese su opcion: "))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificacion()

    # El metodo cargar de la clase Agenda pregunta al usuario por un nombre, telefono y email para despues añadirlo a la lista
    def cargar(self):
        nombre=input("Nombre de la persona: ")
        telefono=input("Telefono: ")
        mail=input("Mail: ")
        self.contactos[nombre]=(telefono,mail)
        print("_"*20)

    # El metodo listado de la clase Agenda muestra por pantalla todos los elementos de la lista
    def listado(self):
        print("Listado de la agenda")
        for nombre, info in self.contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {info[0]}, Email: {info[1]}")
        print("_"*20)

    # El metodo consulta de la clase Agenda muestra un contacto de la lista si existe y si no muetsra un mensage
    def consulta(self):
        nombre=input("Ingrese el nombre de la persona a consultar: ")
        if nombre in self.contactos:
            print(f"{nombre}, su telefono es {self.contactos[nombre][0]} y su email es {self.contactos[nombre][1]}")
        else:
            print("No existe un usuario con dicho nombre")
        print("_"*20)

    # El metodo modificacion de la clase Agenda modifica el contacto con el nombre introducido y si no existe el contaco muestra un mensage
    def modificacion(self):
        nombre=input("Ingrese el nombre de la persona a modificar su telefono y email: ")
        if nombre in self.contactos:
            telefono=input("Ingrese nuevo telefono: ")
            mail=input("Ingrese nuevo mail: ")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un usuario con dicho nombre")

agenda=Agenda()
agenda.menu()