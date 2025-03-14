#esercizio 8.7

def make_album(artist_name:str,album_name:str,number_songs:int = None): 
   if number_songs == None: 
      return{"artist_name":artist_name,"album_name":album_name}
   else: 
     return{"artist_name": artist_name,"album_name":album_name,"number_songs":number_songs}
   
print(make_album("giorgia","Oronero","5"))
print(make_album("Adele","19"))
print(make_album("Sam Smith","The Thrill of It All","14"))
