import math
import networkx as nx
import matplotlib.pyplot as plt

def compute_stats(numbers):
    """
    Computes Mathematical Functions given a set of numbers.
    """
    visited_nodes = []
    visited_nodes.append("1") # Start
    visited_nodes.append("2") # Initialize variables
    length = len(numbers)
    sum_values = 0
    
    # Loop to calculate the sum
    visited_nodes.append("3") # Loop to calculate the sum
    for i in range(length):
        visited_nodes.append("4") # sum_values += numbers[i]
        sum_values += numbers[i]
        visited_nodes.append("3")
    
    visited_nodes.append("5") # Sort the numbers to find the median
    # Sort the numbers to find the median
    numbers_sorted = sorted(numbers)
    median = numbers_sorted[length // 2]
    # Calculate the mean
    mean = sum_values / length
    varsum = 0
    
    # Loop to calculate the variance sum
    visited_nodes.append("6") # Loop to calculate the variance sum
    for i in range(length):
        visited_nodes.append("7")
        varsum += (numbers[i] - mean) ** 2
        visited_nodes.append("6")
    
    visited_nodes.append("8") # Calculate the variance
    # Calculate the variance
    variance = varsum / (length - 1)
    # Calculate the standard deviation
    standard_deviation = math.sqrt(variance)
    # Print the results
    print(f"length: {length}")
    print(f"mean: {mean}")
    print(f"median: {median}")
    print(f"variance: {variance}")
    print(f"standard deviation: {standard_deviation}")
    print(f"Visited Nodes: {visited_nodes}\n")

def create_cfg():
    """
    Generates a Control Flow Graph (CFG) for the compute_stats function.
    """
    cfg = nx.DiGraph()

    # Nodes representing different parts of the program
    cfg.add_nodes_from([
        "1", "2", "3", "4", "5", "6", "7", "8"
    ])

    # Edges representing control flow
    edges = [
        ("1", "2"),
        ("2", "3"),
        ("3", "4"),
        ("4", "3"),  # Loop back
        ("3", "5"),
        ("5", "6"),
        ("6", "7"),
        ("7", "6"),  # Loop back
        ("6", "8")
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
        ("4", "3"): "Loop through numbers",
        ("3", "5"): "Exit for loop",
        ("7", "6"): "Loop through numbers",
        ("6", "8"): "Exit for loop"
    }
    
    # Draw edge labels
    nx.draw_networkx_edge_labels(cfg, pos, edge_labels=edge_labels, font_color='red')
    
    plt.title("Control Flow Graph of compute_stats Function")
    plt.show()

# Test case 1: Normal case with positive numbers
numbers = [1, 2, 3, 4, 5]
compute_stats(numbers)

# Test case 2: Case with negative numbers
numbers = [-1, -2, -3, -4, -5]
compute_stats(numbers)

# Test case 3: Case with mixed positive and negative numbers
numbers = [-1, 2, -3, 4, -5]
compute_stats(numbers)

# Test case 4: Case with all zeros
numbers = [0, 0, 0, 0, 0]
compute_stats(numbers)
"""
# Test case 5: Case with a single element
numbers = [1]
compute_stats(numbers)
# Test case 6: Case with an empty array (length 0)
numbers = []
compute_stats(numbers)
"""
# Generate and display CFG
cfg = create_cfg()
draw_cfg(cfg)