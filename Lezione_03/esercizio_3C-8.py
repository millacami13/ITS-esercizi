#Esercizio 3C-8

frase:str = input (f" Inserire frase: ")

match frase:
    case frase if frase [-1] == ('?') and len(frase) %2 == 0:
        print ("Si")
    case frase if frase [-1] == ('?') and len(frase) %2 != 0:
        print ("No")
    case frase if frase [-1] == ('!'):
        print ("Wow")
    case _:
        print(f"Tu dici \"{frase}\"")
