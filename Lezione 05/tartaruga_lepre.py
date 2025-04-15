import random

position_list: list [int] = []

for i in range [1,71]:
    position_list.append (i)

random_number = random.randint (1, 10)

def mossaTurtle():
    match random_number:
        case random_number if 1 <= random_number <= 5:
            pos_turtle = position_list[+3]
        case random_number if 6 <= random_number <= 7:
            pos_turtle = position_list[-6]
            if pos_turtle < 1:
                pos_turtle = position_list[0]
        case random_number if 8 <= random_number <= 10:
            pos_turtle = position_list[+1]
