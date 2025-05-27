from tipi_di_dato import *
from datetime import date

class Impiegato:

    _nome:str
    _cognome:str
    _nascita:date
    _stipendio:RealGEZ
    
    def __init__(self, nome:str, cognome:str, nascita: date,stipendio:RealGEZ):
        self.set_nome = nome
        self.set_cognome = cognome
        self._nascita:date = nascita
        self.set_stipendio = stipendio

    def set_nome(self, nome:str) -> None:
        self._nome:str = nome

    def get_nome(self) -> str:
        return self._nome    

    def set_cognome(self, cognome:str) -> None:
        self._cognome:str = cognome

    def get_cognome(self) -> str:
        return self._cognome    

    def set_stipendio(self, stipendio:RealGEZ) -> None:
        self._stipendio:RealGEZ = stipendio

    def get_stipendio(self) -> RealGEZ:
        return self._stipendio

    def get_nascita(self) -> date:
        return self._nascita
    
class Dipartimento:

    _nome:str
    _telefono:str
    _indirizzo:Indirizzo

    def __init__(self, nome:str, indirizzo:Indirizzo, telefono:Telefono):
          self.set_nome = nome
          self.set_telefono = telefono
          self.set_indirizzo = indirizzo
    
    def set_nome(self, nome:str) -> None:
        self._nome:str = nome

    def get_nome(self) -> str:
        return self._nome 
    
    def set_indirzzo(self, indirizzo:Indirizzo) -> None:
        self._indirizzo:Indirizzo = indirizzo

    def get_indirizzo(self) -> Indirizzo:
        return self._indirizzo

    def set_telefono(self, telefono:Telefono) -> None:
        self._telefono:Telefono = telefono

    def get_telefono(self) -> frozenset [Telefono]:
        return frozenset[Telefono]

class Progetto:

    _nome:str
    _budget:RealGEZ

    def __init__(self, nome:str, budget:RealGEZ):
        self.set_nome = nome
        self.set_budget = budget

    def set_nome(self, nome:str) -> None:
        self._nome:str = nome

    def get_nome(self) -> str:
        return self._nome 

    def set_budget(self, budget:RealGEZ) -> None:
        self._budget:RealGEZ = budget

    def get_budget(self) -> RealGEZ:
        return self._budget                
             


    




        
        