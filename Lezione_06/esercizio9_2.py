#esercizio 9.2

class Resturant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.resturant_name = restaurant_name
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        print (f"{self.resturant_name} : {self.cusine_type}")

ristorante : Resturant = Resturant ("Sant'Isidoro", "Pizza")
ristorante2: Resturant = Resturant ("La pergola", "Pesce")
ristorante3: Resturant = Resturant ("Kilo", "Carne")

ristorante.describe_restaurant ()
ristorante2.describe_restaurant ()
ristorante3.describe_restaurant ()

