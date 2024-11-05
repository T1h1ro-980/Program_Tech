import math


def Quad_equ(a, b, c):
    D = (b**2 - 4*a*c)
    assert D >= 0, "Отрицательный дискрименант"
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    return (x1,x2)