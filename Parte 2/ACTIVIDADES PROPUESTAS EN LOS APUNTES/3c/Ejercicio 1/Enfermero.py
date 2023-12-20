from Persona import Persona

class Enfermero(Persona):
    def __init__(self, dn, n, direc, tele, p):
        super().__init__(dn, n, direc, tele)
        self.planta = p