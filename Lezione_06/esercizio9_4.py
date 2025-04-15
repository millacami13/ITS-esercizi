#esercizio 9.4

class Restaurant:
    def __init__ (self, restaurant_name:str, cusine_type:str, number_served:int = 0):

        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print (f" {self.restaurant_name} : {self.cusine_type}")  

    def open_restaurant(self):
        print (f" {self.restaurant_name} is open")

    def set_number_served(self):
        print (f" The number of the clients is: {self.number_served}")

    def increment_number_served(self):
        print (self.number_served + 30)


ristorante: Restaurant = Restaurant ("Sant'Isidoro", "Pizza", 13)
ristorante.describe_restaurant()
ristorante.open_restaurant()
ristorante.set_number_served()
ristorante.increment_number_served()