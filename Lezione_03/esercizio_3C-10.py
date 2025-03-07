#Esercizio 3C-10

day:int = int (input (f" Inserire il giorno: "))
month:int = int (input (f" Inserire il mese: "))

date:tuple = (day, month)

match date:
    case (1, 1):
        print (f" Il 1/1 è Capodanno")
    case (14, 2):
        print (f" Il 14/02 è San Valentino")
    case (2, 6):
        print (f" Il 2/6 è la Festa della Repubblica Italiana")
    case (15, 8):
        print (f" Il 15/8 è Ferragosto")
    case (31, 10):
        print (f" Il 31/10 è Halloween")
    case (25, 12):
        print (f" Il 25/12 è Natale")
    case _:
        print (f" Nessuna festività importante in questa data")

#giorni_per_mese:list [int] = [31, 29, 31, 30, 31, 30, 31, 31, ]        