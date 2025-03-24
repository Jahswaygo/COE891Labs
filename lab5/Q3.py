from enum import Enum

class Triangle(Enum):
    SCALENE = "SCALENE"
    ISOSCELES = "ISOSCELES"
    EQUILATERAL = "EQUILATERAL"
    INVALID = "INVALID"

def triangle_type(s1, s2, s3):
    # Reachability predicates
    if s1 <= 0 or s2 <= 0 or s3 <= 0:  # P1: Non-positive sides
        return Triangle.INVALID
    if s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2:  # P2: Triangle inequality
        return Triangle.INVALID
    if s1 == s2 == s3:  # P3: Equilateral triangle
        return Triangle.EQUILATERAL
    if s1 == s2 or s2 == s3 or s1 == s3:  # P4: Isosceles triangle
        return Triangle.ISOSCELES
    return Triangle.SCALENE  # P5: Scalene triangle