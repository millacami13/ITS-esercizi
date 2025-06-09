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

     
    
    
 


            


 