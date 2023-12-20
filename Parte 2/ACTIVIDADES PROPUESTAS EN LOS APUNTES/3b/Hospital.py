class Persona:
    def __init__(self, dn, n, direc, tele):
        self.dni = dn
        self.nombre = n
        self.direccion = direc
        self.telefono = tele


class Medico(Persona):
    def __init__(self, dn, n, direc, tele, e):
        super().__init__(dn, n, direc, tele)
        self.especialidad = e


class Enfermero(Persona):
    def __init__(self, dn, n, direc, tele, p):
        super().__init__(dn, n, direc, tele)
        self.planta = p


class Administrativo(Persona):
    def __init__(self, dn, n, direc, tele):
        super().__init__(dn, n, direc, tele)


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


class Consulta:
    def __init__(self, f, m):
        self.fecha = f
        self.medico = m

print("Creando médicos...")
m1 = Medico(123, "Medico1", "C/Medico1", 123, "Alergología")
m2 = Medico(456, "Medico2", "C/Medico2", 456, "Cardiología")
m3 = Medico(789, "Medico3", "C/Medico3", 789, "Inmunología")
print("Médicos creados.")

print("\nCreando enfermeros...")
personal = [
    Enfermero(321, "Enfermero1", "C/Enfermero1", 321, 1),
    Enfermero(654, "Enfermero2", "C/Enfermero2", 654, 2),
    Enfermero(987, "Enfermero3", "C/Enfermero3", 987, 3)
]
print("Enfermeros creados.")

print("\nCreando cliente...")
cliente = Cliente(147, "Cliente", "C/Cliente", 147)
print("Cliente creados.")

print("\nCreando consultas...")
consultas = [
    Consulta("14/12/2023", m1),
    Consulta("15/12/2023", m2),
    Consulta("16/12/2023", m3)
]
print("Consultas creadas.")

print("\nIntroduciendo consultas en el cliente...")
cliente.consultas = consultas
print("Consultas introducidas en el cliente.")

print("\nMostrando cliente: \n")
cliente.mostrar_informacion()