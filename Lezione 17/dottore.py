from persona import Persona
class Dottore(Persona):

    def __init__(self, first_name, last_name, specialization: str, parcel:float):
        super().__init__(first_name, last_name)
