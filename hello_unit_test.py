import unittest


def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiply(x, y):
    return x * y


class TestCalculation(unittest.TestCase):
    def test_2つの整数の和を計算できる(self):
        self.assertEqual(7, add(3, 4))

    def test_2つの整数の差を計算できる(self):
        self.assertEqual(1, subtraction(4, 3))

    def test_2つの整数の積を計算できる(self):
        self.assertEqual(8, multiply(2, 4))


if __name__ == '__main__':
    unittest.main()
