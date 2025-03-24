class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

alice = Person ("Alice W.", 45)
bob = Person ("Bob M.", 36)

#Point 1
print (f"Età di Bob: {bob.age}")

#Point 2
if alice.age > bob.age:
    print (f"{alice.name} è il più vecchio")
else:
    print (f"{bob.name} è il più vecchio")

oldest_name = alice.name if alice.age > bob.age else bob.name
print (f"{oldest_name} è il più vecchio")

#Point 3
person_list = [alice, bob]
for i in range (3):
    person_list.append (Person(f"Persona_{i}" , i+40))

print (len(person_list)) 

#Point 4
person = person_list [0]
for p in person_list [1:]:
    if p.age < person.age:
        person = p

print (f"Il più giovane è: {person.name}")        