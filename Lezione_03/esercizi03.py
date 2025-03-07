#es1.2

posti_max:int = int (input (" Inserisci numero max di posti: "))
posti_liberi = posti_max

while True:
    opzione:str = input (" Inserisci opzione: ")
    if opzione == "ingresso":
        if posti_liberi > 0:
            posti_liberi -= 1
        else:
            print (" Il parcheggio è pieno")
    elif opzione == "uscita":
        if posti_liberi < posti_max:
            posti_liberi += 1
        else:
            print (" Il parcheggio è già vuoto") 
    elif opzione == "stato":
        print (posti_liberi)
        print (posti_max - posti_liberi)
    elif opzione == "esci":
        break
    else:
        print (" Errore selezionare una scelta tra quelle disponibili")

#es2.2

num_NS:int = int (input (" Inserisci numero veicoli nord-sud: "))
num_EO = int (input (" Inserisci numero veicoli est-ovest: "))
soglia:int = int (input (" Inserisci valore: "))
tempo_priorità:int = int (input (" Inserisci valore: "))

if num_NS > soglia:
    if num_EO > soglia:
        tempo_NS = 50
        tempo_EQ = 50
    else:
        tempo_NS = tempo_priorità
        tempo_EQ = (100 - tempo_priorità)
    if num_EO > soglia:
        tempo_NS = (100 - tempo_priorità)
        tempo_EQ = tempo_priorità
    else:
        veicoli_tot = (num_NS + num_EO)
        tempo_NS = (num_NS / veicoli_tot) * 100
        tempo_EQ = (100 - tempo_NS)
print (tempo_EQ)
print (tempo_NS) 

#es3.2

nome_corso:str = input (" Inserisci il nome del corso: ")
max_posti:int = 100

while True:
    opzione:str = input (" Inserisci opzione: ")
    if opzione == "iscrivi":
        if max_posti > 0:
            max_posti -= 1
        else:
            print (" Non ci sono posti disponibili")
    elif opzione == "annulla":
        if max_posti < 100:
            max_posti += 1
        else:
            print (" Tutt i posti sono già dispoibile")
    elif opzione == "visualizza":
        print ( max_posti)
        print ( 100 - max_posti)
    elif opzione == "elimina ":
        nome_corso:str = input (" Inserisci il nome del corso: ")
    elif opzione == "esci":
        break    
                             
#es4.2

n_tutor:int = 10
attesa:int = 0

# 5 7 8 9 14 15 18 19


#es5.2

n:int = int (input(f" Inserisci numero: "))

if n % 1 == 0 and n > 0:
    somma:int = 0
    i = 0
    while i <= n:                   #for i in tange 81, n+1) rimuovendo i +=1
        somma = (somma + (i *i))
        i += 1
    print (f" La somma è {somma}")
else:
    print (" Errore, n deve essere positivo")    

#es7.2

# cont: int = 0 
# somma:int = 0

# while True:
#     scelta: str = input (f" Inserire scelta: ")
#     if scelta == "si":
#         voto:int = int (input(f" Inserire voto: "))
#         if voto >= 0:
#             somma += voto
#             cont += 1
#         else:
#             print ("errore")

#es8.2





