# Python function to multiply an integer by 2
def multiply_by_two(x):
    """
    This function takes an integer x and returns the integer multiplied by 2.
    
    Parameters:
    x (int): The integer to be multiplied.
    
    Returns:
    int: The result of multiplying x by 2.
    """
    return x * 2

# Unit test script using Python's unittest framework
import unittest

class TestMultiplyByTwo(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(multiply_by_two(2), 4)
    
    def test_zero(self):
        self.assertEqual(multiply_by_two(0), 0)
    
    def test_negative_integer(self):
        self.assertEqual(multiply_by_two(-1), -2)
    
    def test_large_positive_integer(self):
        self.assertEqual(multiply_by_two(1000000), 2000000)

if __name__ == '__main__':
    unittest.main()