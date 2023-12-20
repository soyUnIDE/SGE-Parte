from Persona import Persona

class Medico(Persona):
    def __init__(self, dn, n, direc, tele, e):
        super().__init__(dn, n, direc, tele)
        self.especialidad = e