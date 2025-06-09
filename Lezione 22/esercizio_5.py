#5) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
#dato valore intero definito threshold (soglia)

def prodotto (list_3:list [int], threshold:int = 30) -> int:
    prodotto_1:int = 1 

    for element in list_3:
        if element < threshold:
            prodotto_1 *= element

    return prodotto_1