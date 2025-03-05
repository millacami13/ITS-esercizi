#esercizio 6.2

favourite_number:dict[str, int] = {"Luca":21, "Matteo":69,"Camilla":13,"Fra":71,"Thomas":90}
for i in favourite_number.items():   #.items sia chiavi che valori ; .values solo valori
    print(i)