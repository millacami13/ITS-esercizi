#esercizio 4.11

lista_pizza: list[str] = ["Diavola", "Pistacchiosa", "Margherita"]
friend_pizzas: list[str] = ["Diavola", "Pistacchiosa", "Margherita"]

lista_pizza.append ("Vegetariana")
friend_pizzas.append ("Napoli")

for i in lista_pizza:
    print (f" Le mie pizze preferite sono: \n {i}")
for i in friend_pizzas:
    print (f" Le pizze preferite del mio amico sono: \n {i}")
