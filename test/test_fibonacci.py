import unittest
from parameterized import parameterized

class BaseFibonacciTests(unittest.TestCase):
    def get_fibonacci_function(self):
        pass   

    def test_canary(self):
        self.assertTrue(True)
        
    @parameterized.expand([
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 8),
        (8, 34),
        (10, 89),
    ])
    def test_fibonacci_for_valid_position(self, position, expected):
        fibonacci_function = self.get_fibonacci_function()
        if fibonacci_function is not None: 
            self.assertEqual(expected, fibonacci_function(position))
        
    def test_fibonacci_for_invalid_position(self):
        fibonacci_function = self.get_fibonacci_function()
        if fibonacci_function is not None:
            self.assertRaisesRegex(ValueError, "The number should be non-negative", fibonacci_function, -1)
        