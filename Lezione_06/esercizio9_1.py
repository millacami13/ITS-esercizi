#esercizio 9.1

class Resturant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.resturant_name = restaurant_name
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        print (f"{self.resturant_name} : {self.cusine_type}")

    def open_restaurant(self):
        print (f"{self.resturant_name} is open ")


ristorante : Resturant = Resturant ("Sant'Isidoro", "Pizza")
ristorante.describe_restaurant () 
ristorante.open_restaurant ()