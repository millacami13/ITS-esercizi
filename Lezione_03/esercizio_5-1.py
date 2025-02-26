#esercizio 5.1

cars:str = input (f" Inserisci modello macchina: ")
predicte:bool

if cars == "Audi":
    predicte = True
    print (f" {cars} == macchina? {predicte}")
elif cars == "Bmw":
    predicte = True
    print (f" {cars} == macchina? {predicte}")
elif cars == "Mercedes":
    predicte = True
    print (f" {cars} == macchina? {predicte}")
elif cars == "Ferrari":
    predicte = True
    print (f" {cars} == macchina? {predicte}")
elif cars == "Lamborghini":
    predicte = True
    print (f" {cars} == macchina? {predicte}")
elif cars == "Bicicletta":
    predicte = False
    print (f" {cars} == macchina? {predicte}")
elif cars == "Ducati":
    predicte = False
    print (f" {cars} == macchina? {predicte}")
elif cars == "Ktm":
    predicte = False
    print (f" {cars} == macchina? {predicte}")
elif cars == "Sh":
    predicte = False
    print (f" {cars} == macchina? {predicte}")
elif cars == "Kawasaki":
    predicte = False
    print (f" {cars} == macchina? {predicte}")
else:
    print (" La macchina inserita non è presente in elenco")          

