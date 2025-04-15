#esercizio 8

studenti:list [dict] = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

list_decrescente_media:list [dict] = sorted (studenti, key=lambda studente: list(studenti(reverse=True)))
print (list_decrescente_media)