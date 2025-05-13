from typing import Self, Any

class Persona(object): #object super classe della classe Persona

    nome: str
    cognome: str

    def __new__(cls, *args, **kwargs) -> Self:  #costruttore per personalizzare l'oggetto prima che venga inizializzato
        return super().__new__(cls)
    
    def __init__(self, nome:str) -> None: #inizializzatore
        self.nome = nome

    def __eq__(self, other: Any) -> bool:
        if not isinstance (other, type(Self)): #se other non è istanza della classe Persona, uguaglianza è falsa
            return False
        return self.nome == other.nome  #se è una persona controllo il nome
    
    def __hash__(self) -> int:  #restituisce hash oggetto
        return hash
     
        
if __name__== "main":
    alice1:Persona = Persona("Alice")
    print (type(alice1))
    print ("Superclasse di Persona: " + str(Persona.mro ()[-1])) #mro ordine lista dei tipi e supertipi della classe

    alice2:Persona = Persona("Alice")

        