#Esercizio 3C-7

i = 0
countTesta:int = 0
countCroce:int = 0
while i < 8:
    lancio = (input("Inserisci il simbolo che è uscito(t o T --- testa, c o C --- croce): "))
    
    match lancio:
        case lancio if lancio == "t" or lancio =="T":
            countTesta +=1
        case lancio if lancio == "c" or lancio =="C":
            countCroce +=1
        case _:
            print("Non sono stati effettuati lanci")
    i+=1

print(f"Il totale delle teste è {countTesta} mentre la percentuale è {(countTesta *100)/i:.2f}%")
print(f"Il totale delle croci è {countCroce} mentre la percentuale è {(countCroce *100)/i:.2f}%")














