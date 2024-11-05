import Sqrt

def test1():
    assert Sqrt.Quad_equ(1,5) == (0, -5)

def test2():
    assert Sqrt.Quad_equ(8,-14,5) == (1.25, 0.5)

def test3():
    assert Sqrt.Quad_equ(1,-1,-6) == (3, -2)