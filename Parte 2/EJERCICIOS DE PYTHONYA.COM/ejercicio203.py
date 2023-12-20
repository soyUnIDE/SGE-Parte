# La clase Cliente guarda dos variables llamadas nombre y codigo y tiene una variable que es compartida por todos los objetos que es de tipo lista llamada suspendidos
class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    # La funcion imprimir de la clase Cliente muestra por pantalla el codigo, el nombre del cliente y si se encuantra en la lista compartida suspendidos
    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)
        self.esta_suspendido()

    # La funcion esta_suspendido de la clase Cliente muestra por pantalla si el cliente esta en la lista compartida llamada suspendidos
    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    # La funcion suspender de la clase Cliente introduce al cliente en la lista de suspendidos
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)


# bloque principal

cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()   
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)