import unittest
from calculator import sumar, restar, Dividir, Multiplicar


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(-2, 2), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)
        self.assertEqual(restar(5, 5), 0)

    def test_dividir(self):
        self.assertEqual(Dividir(10, 2), 5)
        self.assertEqual(Dividir(9, 3), 3)

    def test_multiplicar(self):
        self.assertEqual(Multiplicar(4, 5), 20)
        self.assertEqual(Multiplicar(-2, 3), -6)


if __name__ == '__main__':
    unittest.main()