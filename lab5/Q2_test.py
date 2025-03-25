import unittest
from Q2 import create_cfg, simulate_program


class TestQ2(unittest.TestCase):
    # Test the control flow graph (CFG)
    def test_cfg(self):
        G = create_cfg()
        self.assertTrue(G.has_edge("Start", "1"))
        self.assertTrue(G.has_edge("10", "End"))
        self.assertFalse(G.has_edge("1", "End"))

    def test_all_def_coverage(self):
        # Initialize a set to collect all unique visited nodes
        unique_visited_nodes = set()

        # Run the program with different inputs and collect visited nodes
        for y in [1,10]:
            visited_nodes = simulate_program(y)
            unique_visited_nodes.update(visited_nodes)  # Add visited nodes to the set

        # Check if all required nodes are in the unique visited nodes
        required_nodes = {"1", "4", "5", "6", "8", "9"}
        self.assertTrue(required_nodes.issubset(unique_visited_nodes), 
                        f"Missing nodes: {required_nodes - unique_visited_nodes}")
        
    def test_all_use_coverage(self):
        # Initialize a set to collect all unique visited nodes
        unique_visited_nodes = set()

        # Run the program with different inputs and collect visited nodes
        for y in [1,10]:
            visited_nodes = simulate_program(y)
            unique_visited_nodes.update(visited_nodes)  # Add visited nodes to the set

        # Check if all required nodes are in the unique visited nodes
        required_nodes = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
        self.assertTrue(required_nodes.issubset(unique_visited_nodes), 
                        f"Missing nodes: {required_nodes - unique_visited_nodes}")
        
        
    def test_all_du_paths_coverage(self):
        # Initialize a set to collect all unique transitions (edges)
        unique_transitions = set()
    
        # Run the program with different inputs and collect visited transitions
        for y in [1, 10]:
            visited_nodes = simulate_program(y)
            # Collect transitions as pairs of consecutive nodes
            transitions = [(visited_nodes[i], visited_nodes[i + 1]) for i in range(len(visited_nodes) - 1)]
            unique_transitions.update(transitions)  # Add transitions to the set
    
        # Define the required transitions (edges) for all-DU-paths coverage
        required_transitions = {
            ("Start", "1"), ("1", "2"), ("2", "3"), ("2", "10"), ("3", "4"), ("3", "5"),
            ("4", "10"), ("5", "6"), ("5", "7"), ("6", "5"), ("7", "8"), ("7", "9"),
            ("8", "2"), ("9", "2"), ("10", "End")
        }
    
        # Check if all required transitions are in the unique transitions
        self.assertTrue(required_transitions.issubset(unique_transitions),
                        f"Missing transitions: {required_transitions - unique_transitions}")

if __name__ == "__main__":
    unittest.main()