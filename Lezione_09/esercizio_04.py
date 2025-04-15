#esercizio 4

studenti:list [tuple] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]
list_by_age: list [tuple] = sorted (studenti, key=lambda studente: tuple [0](studente))
print (list_by_age)