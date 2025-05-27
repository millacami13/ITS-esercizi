from typing import Self, Any

from enum import *

class Genere (StrEnum):
    uomo = auto()  #auto crea il valore del tipo di dato che è anche una stringa
    donna = auto()

class Continente (StrEnum) :
    asia = auto()
    europa = auto()
    africa = auto()
    america = auto()
    antartide = auto()

class Voto (int):
    def __new__ (cls, v:int|float|Self) -> Self:
        if v < 18 or v > 30:
                raise ValueError (f"Value v == {v} must be between 18 and 30")
        return int. __new__(cls, v)
    
    def __add__(self, other:Self) -> Self:
         return 