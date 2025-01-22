def sum_greater_than_each(a: int, b: int) -> bool:
    # Check if the sum of a and b is greater than each individual number
    return a + b > a and a + b > b

def commutative_property(a: int, b: int) -> bool:
    # Check if the sum of a and b is equal to the sum of b and a
    return a + b == b + a
