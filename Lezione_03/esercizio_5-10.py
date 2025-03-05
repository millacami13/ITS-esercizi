#esercizio 5.10

current_users:list [str] = ["camilla", "matteo", "luca", "francesco", "thomas" "silvia"]
new_users:list [str] = ["camilla", "luca", "mattia", "alessandra", "carlotta"]

for i in current_users:
     if i.lower() in new_users:
         print(f"l'username scelto {i} già è in uso! Sceglierne un'altro.")