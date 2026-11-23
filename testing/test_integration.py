import unittest
from app import add, calculate_total

class TestIntegration(unittest.TestCase):

    def test_order_calculation(self):
        price = add(100, 50)
        total = calculate_total(price, 2)
        self.assertEqual(total, 300)

if __name__ == "__main__":
    unittest.main()
