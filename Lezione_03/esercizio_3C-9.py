#Esercizio 3C-9

point_x: int = int (input (f" Inserire coordinata x: "))
point_y: int = int (input (f" Inserire coordinata y: "))

coordinate: tuple = (point_x, point_y)

match coordinate:
    case coordinate if coordinate == (0, 0):               #si può scrivere case (0,0)
        print (f" Il punto si trova nell'origine")
    case coordinate if coordinate == (point_x, 0):
        print (f" Il punto si trova sull'asse X")
    case coordinate if coordinate == (0, point_y):
        print (f" Il punto si trova sull'asse Y")
    case coordinate if point_x > 0 and point_y > 0:         # si può scrivere case (x, y) if x>0 y>0
        print (f" Il punto si trova nel primo quadrante")   
    case coordinate if point_x < 0 and point_y > 0:
        print (f" Il punto si trova nel secondo quadrante")
    case coordinate if point_x < 0 and point_y < 0:
        print (f" Il punto si trova nel terzo quadrante")
    case coordinate if point_x > 0 and point_y < 0:
        print (f" Il punto si trova nel quarto quadrante")    