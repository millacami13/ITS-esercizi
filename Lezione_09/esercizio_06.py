#esercizio 6

from functools import reduce

numeri:list [int] = [2, 3, 4]
prodotto = reduce (lambda numero1, numero2: numero1 * numero2, [2,3,4])
print (prodotto)
