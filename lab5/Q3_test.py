import unittest
from Q3 import triangle_type, Triangle

class TestTriangleType(unittest.TestCase):
    # Test cases for Predicate Coverage (PC)
    def test_predicate_coverage(self):
        self.assertEqual(triangle_type(0, 2, 3), Triangle.INVALID)  # P1: Non-positive side
        self.assertEqual(triangle_type(1, 2, 3), Triangle.INVALID)  # P2: Triangle inequality
        self.assertEqual(triangle_type(3, 3, 3), Triangle.EQUILATERAL)  # P3: Equilateral triangle
        self.assertEqual(triangle_type(3, 3, 5), Triangle.ISOSCELES)  # P4: Isosceles triangle
        self.assertEqual(triangle_type(3, 4, 5), Triangle.SCALENE)  # P5: Scalene triangle

    # Test cases for Clause Coverage (CC)
    def test_clause_coverage(self):
        self.assertEqual(triangle_type(0, 2, 3), Triangle.INVALID)  # s1 <= 0
        self.assertEqual(triangle_type(1, 0, 3), Triangle.INVALID)  # s2 <= 0
        self.assertEqual(triangle_type(1, 2, 0), Triangle.INVALID)  # s3 <= 0
        self.assertEqual(triangle_type(1, 2, 3), Triangle.INVALID)  # Triangle inequality
        self.assertEqual(triangle_type(3, 3, 3), Triangle.EQUILATERAL)  # All sides equal
        self.assertEqual(triangle_type(3, 3, 5), Triangle.ISOSCELES)  # Two sides equal
        self.assertEqual(triangle_type(3, 4, 5), Triangle.SCALENE)  # All sides different

    # Test cases for CACC (Correlated Active Clause Coverage)
    def test_cacc(self):
        self.assertEqual(triangle_type(0, 2, 3), Triangle.INVALID)  # Non-positive side
        self.assertEqual(triangle_type(1, 2, 3), Triangle.INVALID)  # Triangle inequality
        self.assertEqual(triangle_type(3, 3, 3), Triangle.EQUILATERAL)  # All sides equal
        self.assertEqual(triangle_type(3, 3, 5), Triangle.ISOSCELES)  # Two sides equal
        self.assertEqual(triangle_type(3, 4, 5), Triangle.SCALENE)  # All sides different

    # Test for infeasible requirements
    def test_infeasible_requirements(self):
        # A triangle cannot have all sides <= 0 and still satisfy the triangle inequality
        self.assertEqual(triangle_type(-1, -1, -1), Triangle.INVALID)
        # A triangle cannot be both EQUILATERAL and ISOSCELES simultaneously
        self.assertNotEqual(triangle_type(3, 3, 3), Triangle.ISOSCELES)

if __name__ == "__main__":
    unittest.main()