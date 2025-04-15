from persona import Persona
from studente import Studente

#creo un oggetto della classe Persona
cp: Persona = Persona ("Camilla", "Provenzano", 24)

#visualizzare le informazioni relative all'oggetto cp 
print (cp)

#creo un oggetto della classe Studente
studente1: Studente = ("Mario", "Rossi", 20, "0123456")

#visualizzare le informazioni relative a studente1
print (studente1)

#controllo se studente sia istazna della classe Studente
#isitance(obj, Class) -> controlla se l'oggetto obj sia un'istanza della classe Class
#in caso affermativo -> True
#in casp megativo -> False

if isinstance (studente1, Studente):
    print ("\nstudente1 è istanza della classe Studente")

if isinstance (studente1, Persona):
    print ("\nstudente1 è anche istanza della classe Persona")

#controllare se l'oggeto cp è istanza della classe Persona
if isinstance (cp, Persona):
    print ("\nl'pggetto cp è istanza della classe Persona")

#controllare se l'oggetto cp è anche istanza della classe Studemte
if isinstance (cp, Studente):
    print ("\nl'oggeto cp è istanza della classe Persona ed è anche istanza della classe Studnete")
else:
    print ("\nl'oggetto cp è istanza della classe Persona ma non è istanza della classe Studente")

#controllare che la classe Studente sia sottoclasse della classe Persona
#issubclass (Class1, Class2) -> controlla se Class1 sia sottoclasse della classe Class2
#in caso affermativo -> True
#in caso negativo -> False    
if issubclass (Studente, Persona):  #come prima inserire la classe che si vuole controllare
    print ("\nLa classe Studente è sottoclasse della classe Persona")