#4) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
#soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
#è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
#oppure "Azione negata" a seconda delle condizioni che sono soddisfatte

def condizione (X:bool, Y:bool, Z:bool) -> bool:
    if X and (Y or Z):
        return "Azione permessa"
    else:
        return "Azione negata"