#esercizio 8.4

def make_shirt(size:str = "L", msg:str = "I love Python"):
    print (f" La taglia della maglietta è {size} e il messaggio è '{msg}'")

make_shirt ()
make_shirt ("M")
make_shirt ("S", "I love Rome")