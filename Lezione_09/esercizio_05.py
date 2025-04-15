#esercizio 5

from typing import Callable
pari_or_dispari: Callable [[int], str] = lambda num: "pari" if num % 2 == 0 else "dispari"
print (pari_or_dispari (6))
print (pari_or_dispari (3))