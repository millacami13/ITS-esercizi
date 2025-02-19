n:int = int (input("Inserire la posizione:"))

if n == 1:
    print (f" {n}st")
elif n == 2:
    print (f" {n}nd")
elif n == 3:
    print (f" {n}rd")
else:
    n > 3
    print (f" {n}th")
