#esercizio 4.15
#indentation

lista_pizza: list[str] = [
    "Diavola", "Pistacchiosa", "Margherita"
    ]
friend_pizzas: list[str] = [
    "Diavola", "Pistacchiosa", "Margherita"
    ]

lista_pizza.append ("Vegetariana")
friend_pizzas.append ("Napoli")

for i in lista_pizza:
    print (f" Le mie pizze preferite sono: \n {i}")
for i in friend_pizzas:
    print (f" Le pizze preferite del mio amico sono: \n {i}")

#comments

#definisco una lista
lista_animali: list[str] = ["foca", "balena", "narvalo", "pesce rosso"]

#ciclo for
for i in lista_animali:
    print(i)

#ciclo for   
for i in lista_animali:
    print(f" {i} è un animale acquatico")

print("il pesce rosso è un ottimo animale domestico")

#spaces

lista_pizza: list[str] = ["Diavola","Pistacchiosa","Margherita"]
friend_pizzas: list[str] = ["Diavola","Pistacchiosa","Margherita"]

lista_pizza.append ("Vegetariana")
friend_pizzas.append ("Napoli")

for i in lista_pizza:
    print (f" Le mie pizze preferite sono: \n {i}")
for i in friend_pizzas:
    print (f" Le pizze preferite del mio amico sono: \n {i}")
