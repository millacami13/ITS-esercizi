#esercizio 6.10

favourite_number:dict[str, int] = {"Luca": {"primo numero" :21, "secondo numero" : 22}, "Matteo":{"primo numero" :69, "secondo numero":70}, 
                                   "Camilla": {"primo numero" :13, "secondo numero": 27}}

for i in favourite_number.items():   #.items sia chiavi che valori ; .values solo valori
    print(i)