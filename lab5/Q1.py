from itertools import product

# Predicate: p = a ∧ (∼ b ∨ c)
def evaluate_predicate(a, b, c):
    return a and (not b or c)

# Generate truth table for all combinations of (a, b, c)
def generate_truth_table():
    return [(a, b, c, evaluate_predicate(a, b, c)) for a, b, c in product([False, True], repeat=3)]

# Clause determination conditions
def clause_determination():
    return {
        "Clause a": "Determines p when (¬b ∨ c) is True.",
        "Clause ¬b": "Determines p when a is True and c is False.",
        "Clause c": "Determines p when a is True and b is True."
    }

# Generate row pairs for GACC, CACC, RACC, GICC, RICC
def generate_coverage_pairs():
    return {
        "GACC": {
            "Clause a": [(True, False, False), (False, False, False)],
            "Clause ¬b": [(True, True, False), (True, False, False)],
            "Clause c": [(True, True, True), (True, True, False)]
        },
        "CACC": "Same as GACC.",
        "RACC": "Same as GACC.",
        "GICC": {
            "Clause a": [(True, False, False), (False, False, False)],
            "Clause ¬b": [(True, True, False), (True, False, False)],
            "Clause c": [(True, True, True), (True, True, False)]
        },
        "RICC": "Same as GICC."
    }