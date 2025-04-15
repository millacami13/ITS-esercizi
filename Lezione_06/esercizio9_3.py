#esercizio 9.3

class User:
    def __init__(self, first_name:str, last_name:str, age:int, fiscal_code:str):
        self.first_name = first_name
        self.last_name = last_name
        self.fiscal_code = fiscal_code
        self.age = age

    def describe_user(self):
        print (f"First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nFiscal code: {self.fiscal_code}")

    def greet_user(self):
        print (f"Welcome back {self.first_name} {self.last_name}")


cp: User = User ("Camilla", "Provenzano", 24, "PRVCLL00R53H501K")
cp.describe_user()
cp.greet_user()