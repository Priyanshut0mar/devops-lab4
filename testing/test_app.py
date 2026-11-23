import unittest
from app import add, multiply

class TestApplication(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)

    def test_multiplication(self):
        self.assertEqual(multiply(4, 3), 12)

if __name__ == "__main__":
    unittest.main()
