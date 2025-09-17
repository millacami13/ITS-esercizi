class Persona:
    '''
    Di una persona dobbiamo sapere delle informazioni.'
    Queste informazioni vengono chiamate attributi (della classe Persona)
    Le informazioni saranno:
    -nome
    -cognome
    -età

    come li rappresento in Python?

    self.name:str (attributo di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo int)

    '''

    #costruttore della classe Persona
    #crea gli attributi
    def __init__(self, name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age

    #funzione che mostri in output tutt i dati di una persona
    def displayData(self) -> None:
        print (f"Name: {self.name}\nLastname; {self.lastname}\nAge: {self.age}")


cp:Persona = Persona ("Camilla", "Provenzano", 24)   #oggeto o istanza della classe persona 

print (cp)

#mostra i dati di una persona
cp.displayData()

