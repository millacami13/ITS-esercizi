#esercizio 6.7

from typing import Any
person: dict[str,Any] = {"first_name" : "Luca", "last_name" : "D'Ambra", "age" : 21, "city" : "Ischia" }
person2 : dict[str,Any] = {"first_name" : "Matteo", "last_name" : "Argenti", "age" : 21, "city" : "Trullo"}
person3 : dict[str,Any] = {"first_name" : "Thomas", "last_name" : "Marchionni", "age" : 19, "city" : "Acilia"}

people : list[str] = [person, person2, person3]

for i in people:
    print(i)