#esercizio 3

numeri: list [int] = [5, 12, 17, 18, 24, 32]
pari:list [int] = list (filter(lambda numero: numero % 2 == 0, numeri))
print (pari)