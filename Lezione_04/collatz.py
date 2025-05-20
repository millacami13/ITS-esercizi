#congettura di Collatz

# import matplotlib.pyplot as plt

# def f (n:int):
#     if n % 2 == 0:
#         n = n/2
#     else:
#         n = (3*n) + 1

#     return n      

# def collatz (num:int):
#     numero = f(num)   

#     while True:
#         if numero == 1:
#             break
    
#     return 


# CONGETTURA DI COLLATZ

import matplotlib.pyplot as plt  # libreria che serve per fare il garafico della funzione

def collatz (num:float) -> list[float]:
    numeri: list = [num]

    while num != 1:

        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1

        numeri.append(num)
    return numeri

print(collatz(8))

numeri: list[float] = collatz(9.0)
plt.plot(numeri)
plt.show()