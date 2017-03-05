import unittest
from summa import summa, product


class TestSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(summa(6, 7), 13)

    def test2(self):
        self.assertEqual(summa(6, 24), 30)

    def test3(self):
        self.assertEqual(summa(6, 2), 8)


class TestProduct(unittest.TestCase):
    def test1(self):
        self.assertEqual(product(6, 7), 42)

    def test2(self):
        self.assertEqual(product(6, 6), 36)

    def test3(self):
        self.assertEqual(product(6, 2), 12)


if __name__ == '__main__':
    unittest.main()
