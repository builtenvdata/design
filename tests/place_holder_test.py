import unittest


def add(x, y):
    return x + y


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(3, -5), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)


if __name__ == '__main__':
    unittest.main()
