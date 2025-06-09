from tipi_di_dato import *
from typing import Self, Any

class Volo:

    codice:str
    durata_minuti:int

    def __init__(self, codice:str, durata_minuti:int) -> None:
        self.codice = codice
        self.durata_minuti = durata_minuti

    def __hash__(self) -> int:
        return hash (self.codice, self.durata_minuti)
    
    def __eq__(self, other:Any) -> bool:
        if not isinstance (other, Volo):
            return False
        return self.codice == other.codice and self.durata_minuti == other.durata_minuti
    
    def set_codice (self, codice:str) -> None:
        self.codice = codice

    def set_durata_minuti (self, durata_minuti:int) -> None:
        self.durata_minuti = durata_minuti

        if durata_minuti < 0:
            raise ValueError ("La durata del volo non può essere negativa")

    def get_codice(self) -> str:
        return self.codice

    def get_durata_minuti (self) -> int:
        return self.durata_minuti

class Aereporto:

    _nome: str
    _codice: str

    def __init__(self, nome:str, codice:str) -> None:
        self._nome = nome
        self._codice = codice

    def __eq__(self, value) -> bool:
        if not isinstance (value, Aereporto):
            return False
        return self._nome == value._nome and self._codice == value._codice
    
    def __hash__(self) -> int:
        return hash (self._nome, self._codice)
    
    def set_nome(self, nome:str) -> None:
        if not self._nome:
            raise ValueError ("Il nome non può essere vuoto")
        else:
            self._nome = nome

    def set_codice(self, codice:str) -> None:
        if not codice:
            raise ValueError ("Il codice non può essere vuoto")
        else:
            self._codice = codice

    def get_nome(self) -> str:
        return self._nome

    def get_codice(self) -> str:
        return self._codice

class Compagnia:

    _nome:str
    _anno_fondazioen:int

    def __init__(self, nome:str, anno_fondazione:int) -> None:
        self._nome = nome
        self._anno_fondazioen = anno_fondazione

    def __eq__(self, value:Any) -> None:
        if not isinstance (value, Compagnia):
            return False
        return self._nome == value._nome and self._anno_fondazioen == value._anno_fondazioen
    
    def __hash__(self) -> int:
        return hash (self._nome, self._anno_fondazioen)
    
    def set_nome (self, nome:str) -> None:
        if not self._nome:
            raise ValueError ("Il nome della compahnai non può essere vuoto")
        else:
            self._nome =nome
            

                           
        
            
            




           
        