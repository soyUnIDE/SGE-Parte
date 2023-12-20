from Cliente import Cliente
from Consulta import Consulta
from Enfermero import Enfermero
from Medico import Medico


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