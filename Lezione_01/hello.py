print ("Hello World")

mydict:dict = {"key1" : "value1", "key2" : "value2"}

for key in mydict:
    print (key)

for key in mydict:
    print (mydict [key])

for keys, values in mydict.items():
    print(f" chiave: {keys}, valore: {values}")    #da una lista di tuple dove ogni elemento rappresenta la coppia chiave valore

for value in mydict.values():    #resitusice una lista di valori del dizionario senza le chaivi
    print(value)   

for key in mydict.keys():   #restituisce una lista di chaivi del dizionario senza i valori
    print(key)