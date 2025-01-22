import unittest
from app import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        # Initialize triangles before each test
        # t1 is a right triangle with sides 3, 4, 5
        # t2 is another right triangle with sides 5, 4, 3 (same as t1 but sides are in different order)
        # t3 is an isosceles triangle with sides 8, 5, 5
        self.t1 = Triangle(3, 4, 5)
        self.t2 = Triangle(5, 4, 3)
        self.t3 = Triangle(8, 5, 5)

    def test_area_t1(self):
        # Test area calculation for triangle t1
        # The expected area is 6.0
        self.assertAlmostEqual(self.t1.calculate_area(), 6.0, places=2)

    def test_area_t2(self):
        # Test area calculation for triangle t2
        # The expected area is 6.0 (same as t1)
        self.assertAlmostEqual(self.t2.calculate_area(), 6.0, places=2)

    def test_area_t3(self):
        # Test area calculation for triangle t3
        # The expected area is approximately 12.0
        self.assertAlmostEqual(self.t3.calculate_area(), 12.0, places=2)

    def test_area_t1_t2_same(self):
        # Test if the area of t1 and t2 are the same
        # Both t1 and t2 should have the same area of 6.0
        self.assertAlmostEqual(self.t1.calculate_area(), self.t2.calculate_area(), places=2)

    def test_invalid_triangle(self):
        # Test for invalid triangle with sides (3, 4, 100)
        # This should raise a ValueError because the sides do not form a valid triangle
        with self.assertRaises(ValueError):
            Triangle(3, 4, 100).calculate_area()
    pass
    
if __name__ == '__main__':
    unittest.main()
