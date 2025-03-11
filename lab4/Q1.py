import networkx as nx
import matplotlib.pyplot as plt

def power_function(x, y):
    """
    Computes the power function Z = X^Y.
    Handles both positive and negative exponents.
    """
    visited_nodes = []
    
    visited_nodes.append("1")
    print(f"Computing {x}^{y}")
    
    w = abs(y)  # Take absolute value of exponent
    z = 1  # Initialize result
    
    visited_nodes.append("2")
    while w != 0:
        visited_nodes.append("3")
        z = z * x
        w = w - 1
        visited_nodes.append("2")
    visited_nodes.append("4")#End of loop
    
    visited_nodes.append("5") #If y
    if y < 0:  # If exponent is negative, take reciprocal
        visited_nodes.append("6")
        z = 1 / z
    visited_nodes.append("7") #End of if
    print(f"Result: {z}")
    visited_nodes.append("8") #Print Z and End of function
    
    print(f"Visited Nodes: {visited_nodes}")
    return z  # Return value for testing

def create_cfg():
    """
    Generates a simplified Control Flow Graph (CFG) for the power function.
    """
    cfg = nx.DiGraph()

    # Nodes representing different parts of the program
    cfg.add_nodes_from([
        "1", "2", "3", "4", "5", "6", "7", "8"
    ])

    # Edges representing control flow
    edges = [
        ("1", "2"),
        ("2", "3"),  # while true
        ("2", "4"),  # while false, skip loop
        ("3", "2"),  # Loop back
        ("2", "4"), 
        ("4", "5"),
        ("5", "6"),  # if true
        ("5", "7"),  # if false, skip body of if
        ("6", "7"),
        ("7", "8"),  # End of function
    ]

    cfg.add_edges_from(edges)
    return cfg

def draw_cfg(cfg):
    """
    Draws the generated CFG using NetworkX and Matplotlib.
    """
    pos = nx.spring_layout(cfg)  # Position nodes
    plt.figure(figsize=(10, 6))
    nx.draw(cfg, pos, with_labels=True, node_color='lightblue', edge_color='black', font_size=10, node_size=2000)
    
    # Define edge labels
    edge_labels = {
        ("2", "3"): "while true",
        ("2", "4"): "while false",
        ("5", "6"): "if true",
        ("5", "7"): "if false"
    }
    
    # Draw edge labels
    nx.draw_networkx_edge_labels(cfg, pos, edge_labels=edge_labels, font_color='red')
    
    plt.title("Control Flow Graph of Power Function")
    plt.show()

def identify_infeasible_paths():
    # In this program, there are no infeasible paths
    infeasible_paths = []
    return infeasible_paths

def node_coverage_test_cases():
    # Test cases for node coverage
    test_cases = [
        {'X': 2, 'Y': -3},   # Negative Y path travels to all nodes
    ]
    return test_cases

def edge_coverage_test_cases():
    # Test cases for edge coverage
    test_cases = [
        {'X': 2, 'Y': 3},   # positive Y
        {'X': 2, 'Y': 0}    # zero Y
    ]
    return test_cases

def run_test_cases(test_cases):
    for test in test_cases:
        print(f"Test case: {test}")
        power_function(test['X'], test['Y'])

if __name__ == "__main__":
    # Generate and display CFG
    cfg = create_cfg()
    draw_cfg(cfg)

    # Identify infeasible paths
    print("\nInfeasible Paths:", identify_infeasible_paths())
    
    # Provide test cases for node coverage
    print("\nNode Coverage Test Cases:", node_coverage_test_cases())
    run_test_cases(node_coverage_test_cases())

    # Provide test cases for edge coverage
    print("\nEdge Coverage Test Cases:", edge_coverage_test_cases())
    run_test_cases(edge_coverage_test_cases())