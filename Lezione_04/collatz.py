#congettura di Collatz

import matplotlib.pyplot as plt

def f (n:int):
    if n % 2 == 0:
        n = n/2
    else:
        n = (3*n) + 1

    return n      

def collatz (num:int):
    numero = f(num)   

    while True:
        if numero == 1:
            break
    
    return 