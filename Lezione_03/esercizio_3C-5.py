#Esercizio 3C-5

ruoli:dict [str, int] = {"nome" : input (f" Inserire nome: "), "ruolo" : input (f" Inserire ruolo: "), "età" : int(input (f" Inseire età: "))}

match ruoli:
    case {"ruolo" : "Admin"}:
        print ("Accesso completo a tutte le funzionalità.")
    case {"ruolo" : "Moderatore"}:
        print ("Può gestire i contenuti ma non modificare le impostazioni.")
    case {"ruolo" : "Utente adulto", "età" : età} if età >= 18:
        print ("Accesso standard a tutti i servizi.")
    case {"ruolo" : "Utente minorenne", "età" : età} if età <18:
        print ("Accesso limitato! Alcune funzionalità sono bloccate.")
    case {"ruolo" :"Ospite"}:
        print ("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _ :
        print ("Attenzione! Ruolo non riconsciuto! Accesso Negato!") 
