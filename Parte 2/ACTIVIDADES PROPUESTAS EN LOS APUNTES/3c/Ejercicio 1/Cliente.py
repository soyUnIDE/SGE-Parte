from Persona import Persona

class Cliente(Persona):
    def __init__(self, dn, n, direc, tele):
        super().__init__(dn, n, direc, tele)
        self.__consultas = []

    @property
    def consultas(self):
        return self.__consultas

    @consultas.setter
    def consultas(self, c):
        self.__consultas = c

    def mostrar_informacion(self):
        print("Información del Cliente:")
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")

        if self.consultas:
            print("\nConsultas:")
            for consulta in self.consultas:
                print(f"Fecha: {consulta.fecha}")
                print(f"Nombre del médico: {consulta.medico.nombre}")
                print(f"Especialidad del médico: {consulta.medico.especialidad}")
                print("-" * 30)
        else:
            print("No hay consultas registradas.")