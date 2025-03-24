import networkx as nx
import matplotlib.pyplot as plt

# Define the control flow graph (CFG) for the given program
def create_cfg():
    G = nx.DiGraph()
    edges = [
        ("Start", "1"), ("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"),
        ("5", "6"), ("6", "7"), ("7", "8"), ("8", "9"), ("9", "10"),
        ("10", "End"), ("3", "End"), ("6", "8")
    ]
    G.add_edges_from(edges)
    return G

# Define def(n) and use(n) for each node
def get_def_use():
    return {
        "1": {"def": ["x"], "use": ["y"]},
        "2": {"def": [], "use": ["x"]},
        "3": {"def": [], "use": ["x", "y"]},
        "4": {"def": ["x"], "use": ["x"]},
        "5": {"def": [], "use": []},
        "6": {"def": ["z"], "use": ["x"]},
        "7": {"def": ["x"], "use": ["x", "z"]},
        "8": {"def": [], "use": ["x"]},
        "9": {"def": ["y"], "use": ["x"]},
        "10": {"def": ["y"], "use": []},
        "End": {"def": [], "use": []},
    }

# Define DU pairs for each variable
def get_du_pairs():
    return {
        "x": [("1", "2"), ("1", "3"), ("1", "4"), ("1", "6"), ("1", "8"), ("1", "9")],
        "y": [("1", "3"), ("9", "10")],
        "z": [("6", "7")],
    }

# Define infeasible test paths
def get_infeasible_paths():
    return [
        ("3", "4", "5", "6", "8"),  # Path where "break" in node 5 is skipped
        ("6", "7", "8", "9", "10"), # Path where loop in node 6 is skipped
    ]

# Define test sets for coverage
def get_test_sets():
    return {
        "all_def_coverage": [
            ("Start", "1", "2", "3", "End"),  # Covers all definitions
        ],
        "all_use_coverage": [
            ("Start", "1", "2", "3", "4", "5", "6", "8", "9", "10", "End"),  # Covers all uses
        ],
        "all_du_paths_coverage": [
            ("Start", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "End"),  # Covers all DU paths
        ],
    }