class Person:
    personCount = 0

    def __init__(self, name):
        self.name = name
        self.update ()

    @classmethod
    def update (cls):
        cls.personCount += 1    


alice = Person ("Alice")
bob = Person ("Bob")

print (Person.personCount)