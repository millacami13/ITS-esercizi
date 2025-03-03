#Esercizio 3C-6

nome_animale:str = input (f" Innserie animale: ")
habitat:str = input (f" Inserire habitat: ")

match nome_animale:
    case "cane"|"gatto"|"cavallo"|"elefante"|"leone":
        print (f" {nome_animale} appartiene alla categoria dei mammiferi")
    case "serpente"|"lucertola"|"tartaruga"|"coccodrillo":
        print (f" {nome_animale} appartiene alla categoria dei rettili")
    case "aquila"|"pappagallo"|"gufo"|"falco":
        print (f" {nome_animale} appartiene alla categoria degli uccelli")
    case "squalo"|"trota"|"salmone"|"carpa": 
        print (f" {nome_animale} appartiene alla categoria dei pesci")
    case _:
        print (f" Non so dire in quale categoria classificare l'animale {nome_animale} ")  

