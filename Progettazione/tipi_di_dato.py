from typing import Self, Any
import re

class CodiceFiscale(str):
    # gli oggetti di questa classe *sono* stringhe
    #  che rispettano il formato del codice fiscale

    def __new__(cls, cf:str) -> Self:
        cff:str = cf.upper().strip() #rendo la stringa maiuscola e senza spazi iniziali e finali
        if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
            return super().__new__(cls, cf)
        
        raise ValueError (f"La stringa '{cff}' non è un codice fiscale italiano valido")
    
class CAP(str):

    def __new__(cls, cap:str) -> Self:
        if re.fullmatch(r'^\d{5}$', cap):
            return super().__new__(cls, cap)
        
        raise ValueError (f"La stringa '{cap}' non è un CAP italiano valido")    

class RealGEZ(float):
    # tipo di dato specializzato Reale >= 0
    def __new__(cls, v: float|int|str|bool|Self) -> Self:
        n: float = float.__new__(cls,v) # prova a converitre

        if n >= 0:
            return n
        
        raise ValueError (f"Il valore {n} è negativo!")

class Valuta(str):
    def __new__(cls, v:str) -> Self:
        if re.fullmatch(r'^[A-Z]{3}$',v):
            return super().__new__(cls, v)
        raise ValueError(f"La stringa {v} non è un codice valuta")

class Denaro:
    # rappresenta il tipo di dato concettuale composto 
    # con i seguenti campi:
    #  -importo: Reale
    #  -valuta: Valuta
    _importo: float
    _valuta: Valuta

    def __init__(self, imp:float, val: Valuta) -> None:
        self._importo = imp
        self._valuta = val

    def importo(self) -> float:
        return self._importo

    def valuta(self) -> Valuta:
        return self._valuta
    
    def __str__(self) -> str:
        return f"{self.importo()} {self.valuta()}"
        
    def __repr__(self) -> str:
        return f"Denaro: {self.importo()} unità di valuta: {self.valuta()}"

    def __hash__(self) -> int:
        return hash ( (self.importo(), self.valuta()))
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance (other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.importo() == other.importo() and \
            self.valuta() == other.valuta()
    
    def __add__ (self, other: Self) -> Self:
        """Somma self  ad un'altra istanza di Deanro, ma solo se la valuta è la stessa
        Restituisce una nuova istanza di Denaro"""

        if self.valuta() != other.valuta():
            raise ValueError (f"Non posso sommare importi di valute diverse : '{self.valuta} e {other.valuta}")
        
        somma: float = self.importo() + other.importo()
        return Denaro (somma, self.valuta())
    
class FloatDenaro(float):
    _valuta:Valuta
    def __new__(cls, imp:float, val:Valuta) -> Self:
        d = super().__new__(cls, imp)
        
        d._valuta = val
        return d
    
    def importo(self) -> float:
        return self.real
    
    def valuta(self) -> Valuta:
        return self.valuta
    
    def __str__(self) -> str:
        return f"{self.importo()} {self.valuta()}"
        
    def __repr__(self) -> str:
        return f"Denaro: {self.importo()} unità di valuta: {self.valuta()}"

    def __hash__(self) -> int:
        return hash ( (self.importo(), self.valuta()))
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance (other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.importo() == other.importo() and \
            self.valuta() == other.valuta()
    
    def __add__ (self, other: Self) -> Self:
        """Somma self  ad un'altra istanza di Deanro, ma solo se la valuta è la stessa
        Restituisce una nuova istanza di Denaro"""

        if self.valuta() != other.valuta():
            raise ValueError (f"Non posso sommare importi di valute diverse : '{self.valuta} e {other.valuta}")
        
    def __sub__(self, other: Self) -> Self:
        return self + FloatDenaro(-other, other.valuta())   

    
            
class CodiceFiscaleBrutto:
    # gli oggetti di questa classe *contengono* una stringa
    #  che rispetta il formato del codice fiscale

    cf:str

    def __init__(self, cf:str) -> None:
        cff:str = cf.upper().strip() #rendo la stringa maiuscola e senza spazi iniziali e finali
        if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
            self.cf = cff
        else:
            raise ValueError (f"La stringa '{cff}' non è un codice fiscale italiano valido")
        
class Indirizzo:

    _via: str
    _civico : int

    def _init_ (self, via: str, civico: int) -> None:

        self._via = via
        self._civico = civico

    def via(self) -> str:
        return self._via
        
    def civico(self) -> int:
        return self._civico
        
    def _hash_ (self) -> int:
        return hash(self._via, self._civico)
        
    def _eq_ (self, other:Any) -> bool:
            
        if other is None or \
                not isinstance (other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico


class Telefono (str):

    def _new_(cls, telefono: str):

        if re.fullmatch(r"^\+?[1-9][0-9]{7,14}$", telefono):

            return super()._new_(cls, telefono)
        
        else:

            raise Exception("numero di telefono inserito non correttamente")

