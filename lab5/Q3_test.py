import unittest
from Q3 import triangle_type, Triangle

class TestTriangleType(unittest.TestCase):
    # Test cases for Predicate Coverage (PC)
    def test_predicate_coverage(self):
        # P1: Non-positive side
        self.assertEqual(triangle_type(-80, 2, 3), Triangle.INVALID)  # P1 = True
        # P2: Triangle inequality
        self.assertEqual(triangle_type(100, 2, 3), Triangle.INVALID)  # P2 = True
        # P3: Equilateral triangle
        self.assertEqual(triangle_type(3, 3, 3), Triangle.EQUILATERAL)  # P3 = True
        # P4: Isosceles triangle
        self.assertEqual(triangle_type(3, 3, 5), Triangle.ISOSCELES)  # P4 = True
        # P5: Scalene triangle
        self.assertEqual(triangle_type(3, 4, 5), Triangle.SCALENE)  # P5 = True

    # Test cases for Complete Condition Coverage (CC)
    def test_complete_condition_coverage(self):
        # P1: Non-positive side
        self.assertEqual(triangle_type(0, 2, 3), Triangle.INVALID)  # C1.1 = True
        self.assertEqual(triangle_type(1, 0, 3), Triangle.INVALID)  # C1.2 = True
        self.assertEqual(triangle_type(1, 2, 0), Triangle.INVALID)  # C1.3 = True

        # P2: Triangle inequality
        self.assertEqual(triangle_type(1, 2, 3), Triangle.INVALID)  # C2.1 = True
        self.assertEqual(triangle_type(3, 1, 2), Triangle.INVALID)  # C2.2 = True
        self.assertEqual(triangle_type(2, 3, 1), Triangle.INVALID)  # C2.3 = True

        # P3: Equilateral triangle
        self.assertNotEqual(triangle_type(3, 3, 5), Triangle.EQUILATERAL)  # C3.1 = True
        self.assertNotEqual(triangle_type(5, 3, 3), Triangle.EQUILATERAL) # C3.2 = True

        # P4: Isosceles triangle
        self.assertEqual(triangle_type(3, 3, 5), Triangle.ISOSCELES)  # C4.1 = True
        self.assertEqual(triangle_type(5, 3, 3), Triangle.ISOSCELES)  # C4.2 = True
        self.assertEqual(triangle_type(3, 5, 3), Triangle.ISOSCELES)  # C4.3 = True

        # P5: Scalene triangle
        self.assertEqual(triangle_type(3, 4, 5), Triangle.SCALENE)  # All conditions False
    
    # Test cases for Correlated Active Clause Coverage (CACC)
    def test_cacc(self):
        # P1: Non-positive side
        self.assertEqual(triangle_type(0, 2, 3), Triangle.INVALID)  # C1.1 = True
        self.assertEqual(triangle_type(1, 2, 3), Triangle.INVALID)  # C1.1 = False
        self.assertEqual(triangle_type(1, 0, 3), Triangle.INVALID)  # C1.2 = True
        self.assertEqual(triangle_type(1, 2, 0), Triangle.INVALID)  # C1.3 = True

        # P2: Triangle inequality
        self.assertEqual(triangle_type(1, 2, 3), Triangle.INVALID)  # C2.1 = True
        self.assertEqual(triangle_type(3, 4, 5), Triangle.SCALENE)  # C2.1 = False
        self.assertEqual(triangle_type(3, 1, 2), Triangle.INVALID)  # C2.2 = True
        self.assertEqual(triangle_type(2, 3, 1), Triangle.INVALID)  # C2.3 = True

        # P3: Equilateral triangle
        self.assertEqual(triangle_type(3, 3, 3), Triangle.EQUILATERAL)  # C3.1 = True, C3.2 = True
        self.assertNotEqual(triangle_type(3, 3, 5), Triangle.EQUILATERAL)  # C3.1 = True, C3.2 = False

        # P4: Isosceles triangle
        self.assertEqual(triangle_type(3, 3, 5), Triangle.ISOSCELES)  # C4.1 = True
        self.assertEqual(triangle_type(3, 5, 3), Triangle.ISOSCELES)  # C4.2 = True
        self.assertEqual(triangle_type(5, 3, 3), Triangle.ISOSCELES)  # C4.3 = True


if __name__ == "__main__":
    unittest.main()