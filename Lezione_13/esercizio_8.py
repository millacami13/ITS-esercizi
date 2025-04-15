#esercizio 8

#se la stringa è vuota, quante vocali ci sono nella stringa vuota? Nessuna, quindi 0

'''se la stringa non è vuota, ed è ad esempio la stringa "Ciao"
considero il primo carattere della "Ciao", ovvero "C" 
"C" è una vocale? NO quindi 0 vocali + quanteVocaliNellaStringa ("iao")'''

'''considero il primo carattere della stringa ("iao"), ovvero "i"
"i" è una vocale? SI quindi 1 vocale + quanteVocaliNellaStringa ("ao")'''

'''considero il primo carattere della stringa ("ao"), ovvero "a"
"a" è una vocale? SI quindi 1 vocale + quanteVocaliNellaStringa ("o")'''

'''considero il primo carattere della stringa ("o"), ovvero "o"
"o" è una vocale? SI quindi 1 vocale + quanteVocaliNellaStringa ("")'''


def vowelsCounter (s:str) -> int:

    #if s is an empty string, return 0, because is not possible to count any vowel (no vowel found)
    if not s:
        return 0
    
    #if the first char of the string is a vowel, we count a vowel, so add 1 and call vowelCounter to check for the next char of the string s recursively
    if s[0].lower () in ["a", "e", "i", "o", "u"]:
        return 1 + vowelsCounter(s[1:])
    
    #if the first char of the string s is not a vowel, check for the next char in the string s recursively
    else:
        return 0 + vowelsCounter(s[1:])
    
print (f" La stringa \"\" contiene {vowelsCounter("")} vocali")
print (f" La sttringa \"CIAO\" contiene {vowelsCounter("CIAO")} vocali")
print (f" La stringa \"Pappagallo\" contiene {vowelsCounter("Pappagallo")} vocali")
print (f" La stringa \"Ho bisto lei che bacia lui\" contiene {vowelsCounter("Ho visto lei che bacia lui")} vocali")