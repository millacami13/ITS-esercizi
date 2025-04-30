#dal modulo esercizio12_1.py importare la classe MovieCatalog
from esercizio12_1 import MovieCatalog

#creare un oggetto della MovieCatalog
catalog: MovieCatalog = MovieCatalog()

#aggiungiamo un regista e dei film al catalogo
catalog.add_movie('steven spielberg', ['casper', 'ritorno al futuro'])


print (catalog.getCatalog())

#aggiungere un altro film di steven spielberg
catalog.add_movie("steven spielberg", ["ET"])

print (catalog.getCatalog())

#aggiungere un nuovo regista
catalog.add_movie("quentin tarantino", ["pulp fiction", "kill bill"])

print (catalog.getCatalog())

#rimuovere il film "ET" dal catalogo
catalog.remove_movie("steven spielber", "ET")

catalog.remove_movie("steven spielberg", "ritorno al futuro")
catalog.remove_movie("steven spielberg", "casper")