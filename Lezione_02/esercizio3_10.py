#3.10

list_languages:list [str] = ["Francese", "Spagnolo", "Tedesco", "Cinese"]

list_languages.insert (2, "Portoghese")
list_languages.append ("Polacco")
list_languages.pop (2)
del list_languages [1]
list_languages.sort ()
list_languages.reverse ()
print (sorted (list_languages))
print (list_languages)