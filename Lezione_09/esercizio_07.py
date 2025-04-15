#esercizio 7

parole:list [str] = ["cane", "gatto", "elefante", "ratto", "orso"]
parole_4_in_su:list [str] = list (filter(lambda parola: len (parola) > 4, parole))
print (parole_4_in_su)