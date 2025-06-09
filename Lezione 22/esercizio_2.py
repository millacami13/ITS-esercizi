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