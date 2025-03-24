import unittest
from Q2 import create_cfg, get_def_use, get_du_pairs, get_infeasible_paths, get_test_sets

class TestQ2(unittest.TestCase):
    # Test the control flow graph (CFG)
    def test_cfg(self):
        G = create_cfg()
        self.assertTrue(G.has_edge("Start", "1"))
        self.assertTrue(G.has_edge("10", "End"))
        self.assertFalse(G.has_edge("1", "End"))

    # Test def(n) and use(n)
    def test_def_use(self):
        def_use = get_def_use()
        self.assertEqual(def_use["1"], {"def": ["x"], "use": ["y"]})
        self.assertEqual(def_use["11"], {"def": ["y"], "use": []})
        self.assertEqual(def_use["End"], {"def": [], "use": ["x", "y"]})

    # Test DU pairs
    def test_du_pairs(self):
        du_pairs = get_du_pairs()
        self.assertIn(("1", "2"), du_pairs["x"])
        self.assertIn(("9", "10"), du_pairs["y"])
        self.assertIn(("6", "7"), du_pairs["z"])

    # Test infeasible paths
    def test_infeasible_paths(self):
        infeasible_paths = get_infeasible_paths()
        self.assertIn(("3", "4", "5", "6", "8"), infeasible_paths)
        self.assertIn(("6", "7", "8", "9", "10"), infeasible_paths)

    # Test coverage test sets
    def test_test_sets(self):
        test_sets = get_test_sets()
        self.assertIn(("Start", "1", "2", "3", "End"), test_sets["all_def_coverage"])
        self.assertIn(("Start", "1", "2", "3", "4", "5", "6", "8", "9", "10", "End"), test_sets["all_use_coverage"])
        self.assertIn(("Start", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "End"), test_sets["all_du_paths_coverage"])

if __name__ == "__main__":
    unittest.main()