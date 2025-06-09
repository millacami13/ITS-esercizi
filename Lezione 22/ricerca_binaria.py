def Ricercabinaria(lista:list, target:int) -> bool:

    lista_1 = sorted(lista)
    inizio = 0
    fine = len (lista_1) -1

    while inizio <= fine:
        media = (inizio + fine) // 2
        if lista_1 [media] == target:
            return True
        elif lista_1 [media] < target:
            inizio = media + 1
        else:
            fine = media -1

    return False            