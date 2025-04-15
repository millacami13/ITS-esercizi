#esercizo 2

from typing import Callable
somma: Callable [[int, int], int] = lambda a, b: a + b
print (somma (3, 8))