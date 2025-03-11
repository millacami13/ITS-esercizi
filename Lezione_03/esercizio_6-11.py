#esercizio 6.11

cities:dict = {"Parigi" : {"nazione" : "francia", "popolazione" :  2000000, "fact" : "macaron"}, 
               "Berlino" : {"nazione" : "germania", "popolazione" : 3000000, "fact" : "pergamon"},
               "Roma" : {"nazione" : "italia", "popolazione" : 60000000, "fact" : "pizza"}}

for key, value in cities.items():
    print (key, value)