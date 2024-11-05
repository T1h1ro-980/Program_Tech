import unittest

import Sqrt



class SqrtTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Sqrt.Quad_equ(1,5), (0, -5))
    def test2(self):
        self.assertEqual(Sqrt.Quad_equ(8,-14,5), (1.25, 0.5))
    def test3(self):
        self.assertEqual(Sqrt.Quad_equ(1,-1,-6), (3, -2))

unittest.main()