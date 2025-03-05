#esercizio 4

def check_each (myList:list [int]):
    
    for i in myList:
        print (i)

        if i > 5:
            print (f" {i} è maggiore di 5")
        elif i < 5:
            print (f" {i} è minore di 5")    
        else:
            print (f" {i} è uguale a 5")

myList:list [int] = [1, 2, 3, 4]

check_each (myList)
