import math


def Quad_equ(a = 0, b = 0, c = 0):
    D = (b**2 - 4*a*c)
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    return (x1, x2)