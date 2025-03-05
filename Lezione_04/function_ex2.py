#esercizio 2

def check_length (stringa):
    if len (stringa) > 10:
        print (f" La stringa '{stringa}' è maggiore di 10 caratteri")
    elif len (stringa) < 10:
        print (f" La stringa '{stringa}' è minore di 10n caratteri")
    else:
        print (f" La stringa '{stringa}' è di 10 ncaratteri")

check_length (input(f" Inserire stringa: "))                