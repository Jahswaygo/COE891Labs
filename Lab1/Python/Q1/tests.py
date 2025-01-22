import unittest
from app import ArrayMult

class TestArrayMult(unittest.TestCase):
    
    def setUp(self):
        # Initialize the ArrayMult instance before each test
        self.array_mult = ArrayMult()
    
    def test_mult_same_length(self):
        # Test multiplying two arrays of the same length
        result = self.array_mult.mult([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [4, 10, 18])
    
    def test_mult_different_length(self):
        # Test multiplying arrays of different lengths, second array longer
        result = self.array_mult.mult([1, 2], [3, 4, 5])
        self.assertEqual(result, [3, 8, 5])
    
    def test_mult_first_array_longer(self):
        # Test multiplying arrays where the first array is longer
        result = self.array_mult.mult([1, 2, 3, 4], [5, 6])
        self.assertEqual(result, [5, 12, 3, 4])
    
    def test_mult_second_array_longer(self):
        # Test multiplying arrays where the second array is longer
        result = self.array_mult.mult([1, 2], [3, 4, 5, 6])
        self.assertEqual(result, [3, 8, 5, 6])

if __name__ == '__main__':
    unittest.main()