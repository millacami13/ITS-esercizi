#Esercizio 3C-00B

nome:str = input (f" Inserire nome: ")
genere:str = input (f" Inserire genere: ")

match genere:
    case "m":
        print (f" Nome {nome} , Maschio")
    case "f":
        print (f" Nome {nome}, Femmmina")
    case _:
        print (f" {nome} non è possibile generare un documento d'identità")