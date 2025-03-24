import unittest
from Q1 import evaluate_predicate, generate_truth_table, clause_determination, generate_coverage_pairs

class TestQ1(unittest.TestCase):
    # Test the evaluate_predicate function
    def test_evaluate_predicate(self):
        self.assertTrue(evaluate_predicate(True, False, False))  # a=True, b=False, c=False
        self.assertFalse(evaluate_predicate(False, False, False))  # a=False, b=False, c=False
        self.assertTrue(evaluate_predicate(True, True, True))  # a=True, b=True, c=True
        self.assertFalse(evaluate_predicate(True, True, False))  # a=True, b=True, c=False

    # Test the truth table generation
    def test_generate_truth_table(self):
        truth_table = generate_truth_table()
        expected_table = [
            (False, False, False, False),
            (False, False, True, False),
            (False, True, False, False),
            (False, True, True, False),
            (True, False, False, True),
            (True, False, True, True),
            (True, True, False, False),
            (True, True, True, True)
        ]
        self.assertEqual(truth_table, expected_table)

    # Test the clause determination conditions
    def test_clause_determination(self):
        conditions = clause_determination()
        expected_conditions = {
            "Clause a": "Determines p when (¬b V c) is True.",
            "Clause ¬b": "Determines p when a is True and c is False.",
            "Clause c": "Determines p when a is True and b is True."
        }
        self.assertEqual(conditions, expected_conditions)

    # Test the coverage pairs generation
    def test_generate_coverage_pairs(self):
        coverage_pairs = generate_coverage_pairs()
        expected_pairs = {
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
        self.assertEqual(coverage_pairs, expected_pairs)

if __name__ == "__main__":
    unittest.main()