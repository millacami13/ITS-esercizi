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