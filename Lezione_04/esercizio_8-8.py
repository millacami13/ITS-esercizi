#esercizio 8.8

def make_album(artist, title):
    album:dict = {"artist": artist, "title": title}   
    return album

while True:
    artist:str = str(input("Artist: "))
    title:str = str(input("Title: "))

    album = make_album(artist, title)
    print(album)