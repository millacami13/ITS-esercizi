#esercizio 2

#supponiamo m = 1000
#t = 3 mesi

''' se t = 3, significa che sono passati tre mesi
quindi somma disponibile = 1.005 * sommaDopoDueMesi'''

''' se t = 2, significa che sono passati tre mesi
quindi somma disponibile = 1.005 * sommaDopoUnMese'''

''' se t = 1, significa che sono passati tre mesi
quindi somma disponibile = 1.005 * sommaDepostaInizio'''

''' se t = 0, significa che non è passato ancora un mese
quindi la somma disponibile sarà uguale alla somma depositata all'inizio (m = 1000)'''


def compoundInterest (m:float, t:int) -> int:

    # if m is negative
    if m < 0.00:
        print ("Computing compound interest on a negative/null balance is not possible! ")
        return 0.00
    
    # if m is 0, the compound interest is 0
    elif m == 0.00:
        return 0.00
    
    #m must be > 0 
    else:
        #if t is negative or 0, it means that no month has passed yet, so the balance remains m
        if t <= 0:
            return (m, 2)
        
        #otherwise compute the compound interest recursively

        else:
            return round (1.005 * compoundInterest (m, t - 1), 2)
print (f"After 3 months balance is: {compoundInterest (1000.00 , 3)}")        
