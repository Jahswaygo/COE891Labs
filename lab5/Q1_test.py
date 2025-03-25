import unittest
from Q1 import evaluate_predicate, generate_truth_table
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
        
        
    # Test Conditional Clauses 
    def test_clauses(self):
        # Clause a: ((not b) V c) = 1
        ##False
        self.assertFalse(evaluate_predicate(False, False, False))
        self.assertFalse(evaluate_predicate(False, False, True))
        self.assertFalse(evaluate_predicate(False, True, True))
        ##True
        self.assertTrue(evaluate_predicate(True, False, False))
        self.assertTrue(evaluate_predicate(True, False, True))
        self.assertTrue(evaluate_predicate(True, True, True))
        
        # Clause b: a = 1, c = 0
        ##False
        self.assertFalse(evaluate_predicate(True, True, False))
        ##True
        self.assertTrue(evaluate_predicate(True, False, False))
        
        # Clause c: a = 1, b = 1
        ##False
        self.assertFalse(evaluate_predicate(True, True, False))
        ##True
        self.assertTrue(evaluate_predicate(True, True, True))
        
        
        # Test Major Clause Coverage
    def test_coverage_criteria(self):
        # GACC (General Active Clause Coverage) == CACC (Correlated Active Clause Coverage)
        #Clause a
        self.assertNotEqual(evaluate_predicate(True, True, True), evaluate_predicate(False, True, True))
        self.assertNotEqual(evaluate_predicate(True, True, True), evaluate_predicate(False, False,True))
        self.assertNotEqual(evaluate_predicate(True, True, True), evaluate_predicate(False, False, False))
        self.assertNotEqual(evaluate_predicate(True, False, True), evaluate_predicate(False, True, True))
        self.assertNotEqual(evaluate_predicate(True, False, True), evaluate_predicate(False, False, True))
        self.assertNotEqual(evaluate_predicate(True, False, True), evaluate_predicate(False, False, False))
        self.assertNotEqual(evaluate_predicate(True, False, False), evaluate_predicate(False, True, True))
        self.assertNotEqual(evaluate_predicate(True, False, False), evaluate_predicate(False, False, True))
        self.assertNotEqual(evaluate_predicate(True, False, False), evaluate_predicate(False, False, False))
        #Clause b
        self.assertNotEqual(evaluate_predicate(True, True, False), evaluate_predicate(True, False, False))
        #Clause c
        self.assertNotEqual(evaluate_predicate(True, True, True), evaluate_predicate(True, True, False))
        
        #  RACC (Restricted Active Clause Coverage)
        #Clause a
        self.assertNotEqual(evaluate_predicate(True, True, True), evaluate_predicate(False, True, True))
        self.assertNotEqual(evaluate_predicate(True, False, True), evaluate_predicate(False, False, True))
        self.assertNotEqual(evaluate_predicate(True, False, False), evaluate_predicate(False, False, False))
        #Clause b
        self.assertNotEqual(evaluate_predicate(True, True, False), evaluate_predicate(True, False, False))
        #Clause c
        self.assertNotEqual(evaluate_predicate(True, True, True), evaluate_predicate(True, True, False))

        # GICC (General Inactive Clause Coverage) contains RICC (Restricted Inactive Clause Coverage)
        #Clause a
        ##False
        self.assertEqual(evaluate_predicate(False, True, False),evaluate_predicate(True,True, False))
        #Clause b
        ##True
        self.assertEqual(evaluate_predicate(True, True, True),evaluate_predicate(True, False, True))
        ##False
        self.assertEqual(evaluate_predicate(False, True, True),evaluate_predicate(False, False, True))
        self.assertEqual(evaluate_predicate(False, True, True),evaluate_predicate(False, False, False))
        self.assertEqual(evaluate_predicate(False, True, False),evaluate_predicate(False, False, True))
        self.assertEqual(evaluate_predicate(False, True, False),evaluate_predicate(False, False, False))
        #Clause c
        ##True
        self.assertEqual(evaluate_predicate(True, False, True),evaluate_predicate(True, False, False))
        ##False
        self.assertEqual(evaluate_predicate(False, True, True),evaluate_predicate(False, True, False))
        self.assertEqual(evaluate_predicate(False, True, True),evaluate_predicate(False, False, False))
        self.assertEqual(evaluate_predicate(False, True, False),evaluate_predicate(False, False, True))
        self.assertEqual(evaluate_predicate(False,False, True),evaluate_predicate(False, False, False))
if __name__ == "__main__":
    unittest.main()