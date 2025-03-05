#esercizio 6.3

from typing import Any

glossary: dict[str,Any] = {"for": "Permette di ripetere un operazione n numero di volte",
                            "while": "Permette di ripetere una condizione finchè vera",
                            "lower": "converte una stringa in lowercase",
                            "upper": "converte una stringa in uppercase",
                            "if": "permette di controllare una o più variabili in un algoritmo"
}

for i in glossary.keys():
    print(f" {i} \n")
for i in glossary.values():
    print(f" {i} \n")
    