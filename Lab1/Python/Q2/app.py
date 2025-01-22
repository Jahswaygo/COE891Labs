import math

class Triangle:
    def __init__(self, side1, side2, side3):
        # Initialize the sides of the triangle
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # Correct Heron's Formula for area of a triangle
        s = (self.side1 + self.side2 + self.side3) * 0.5
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area
