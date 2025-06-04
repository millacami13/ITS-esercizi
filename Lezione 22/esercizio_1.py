#1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
#la chiave è già presente, somma il valore al valore già associato alla chiave
from typing import Any


def convert(list_1:list[tuple]) -> dict:
    dict_1:dict [Any, Any] = {}
    for element in list_1:
        key, value = element [0], element [1]
        if key in dict_1:
            dict_1 [key] += value
        else:
            dict_1 [key] = value

    return dict_1

#2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
#classifichi i numeri in liste separate per numeri positivi e negativi

def pos_neg(list_2:list [float|int]) -> dict [str, list[float|int]]:
    dict_2:dict [str, list[float|int]] = {"positivi" : [], "negativi" : []}

    for element in list_2:
        if element >= 0:
            dict_2 ["positivi"].append(element)
        else:
            dict_2 ["negativi"].append(element)    

    return dict_2

#3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
#restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
#con i prezzi aumentati del 10% e arrotondati a due cifre decimali     

def esercizio_3 (dict_3:dict [str, float|int]) -> dict [str, float|int]:
    dict_4:dict [str, float|int] = {}

    for key, value in dict_3.items():
        if value <= 50:
            dict_4[key] = value + (value * 0.1)
        else:
            continue

    return dict_4

#1.1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
#soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
#è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
#oppure "Azione negata" a seconda delle condizioni che sono soddisfatte

def condizione (X:bool, Y:bool, Z:bool) -> bool:
    if X and (Y or Z):
        return "Azione permessa"
    else:
        return "Azione negata"
    
#2.1) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
#dato valore intero definito threshold (soglia)

def prodotto (list_3:list [int], threshold:int = 30) -> int:
    prodotto_1:int = 1 

    for element in list_3:
        if element < threshold:
            prodotto_1 *= element

    return prodotto_1

#3.1) 3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
#a) 2, 4, 6, 8, 10, 12, 14
#b) 1, 4, 7, 10, 13
#c) 30, 25, 20, 15, 10, 5, 0
#d) 5, 15, 25, 35, 45       

#esercizio fattoriale

def fattoriale (n:int) -> int:
    if n == 1:
        return 1
     
    
    
 


            


 