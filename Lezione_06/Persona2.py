class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    def displayData(self) -> None:
        print (f"Name: {self.name}\nLastname; {self.lastname}\nAge: {self.age}")

    #mi consente di impostare un valore per setName
    def setName (self, name:str) -> None:
        self.name = name    

    #mi consente di impostare un valore per seLlastname
    def setLastname (self, lastname:str) -> None:
        self.lastname = lastname

    #mi consente di impostare un valore per setAge
    def setAge (self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age           

    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.lastname
    
    def getAge(self) -> str:
        return self.age


#crea un oggetto di tipo Persona
cp:Persona = Persona()

#stampa i dati della Persona creata
cp.displayData()

#impostare il none di una persona
cp.setName ("Camilla")

#impostare il cognome di una persona
cp.setLastname ("Provenzano")

#impostare età di una persona
cp.setAge (24)

#stampa i dati della Persona creata
cp.displayData()


print("----------")
print(cp.getName(), cp.getLastname(), cp.getAge())
