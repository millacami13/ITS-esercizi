#esercizio 4.5

list_number:list[int] = []
for i in range(1,1000001):
    list_number.append(i)
print(min(list_number))
print(max(list_number))
print(sum(list_number))