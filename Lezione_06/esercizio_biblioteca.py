#esercizio classi biblioteca

class Libro:

    def _init_(self):

        self.titolo:str = ""
        self.autore:str = ""
        self.genere:list[str] = []

    def set_titolo(self, titolo:str) -> None:

        self.titolo = titolo

    def set_autore(self, autore:str) -> None:

        self.autore = autore

    def set_genere(self, genere:list[str]) -> None:

        self.genere = genere

    def get_titolo(self) -> str:

        return self.titolo
    
    def get_autore(self) -> str:

        return self.autore
    
    def get_genere(self) -> list[str]:

        return self.genere
    
class Biblioteca:

        def _init_(self):

            self.libri: list[Libro] = []

        def aggiungi(self, libro:Libro):
            
            self.libri.append(libro)

        def lista_libri(self) -> str:

            for item in self.libri:
                print(item.get_titolo())


collezione: Biblioteca = Biblioteca()

#libri
libro1: Libro = Libro()
libro1.set_titolo ("Il piccolo principe")
libro1.set_autore ("Sconosciuto")
libro1.set_genere ("Narrativa")

libro2: Libro = Libro()
libro2.set_titolo ("Harry Potter")
libro2.set_autore ("JK Rowling")
libro2.set_genere ("Fantasy")

collezione.aggiungi(libro1)
collezione.aggiungi(libro2)

collezione.lista_libri()

ma:Libro = Libro()
ma.set_titolo ("Le avventure di Matteo Argenti")
ma.set_autore ("Matteo Argenti")
ma.set_genere ("erotico")

collezione.aggiungi(ma)

collezione.lista_libri()