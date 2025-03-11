import math
import networkx as nx
import matplotlib.pyplot as plt

def is_divisible(a, b):
    return b % a == 0

def print_primes(n):
    """
    Finds and prints n prime integers.
    """
    visited_nodes = []  # visited nodes
    visited_nodes.append(1)  # Start
    visited_nodes.append(2)  # Execution of initialization
    cur_prime = 2  # Value currently considered for primeness
    num_primes = 1  # Number of primes found so far
    primes = [0] * 100  # The list of prime numbers
    primes[0] = 2  # Initialize 2 into the list of primes

    visited_nodes.append(3) # Check Condition of while loop
    while num_primes < n:
        visited_nodes.append(4) # Execution of while loop
        cur_prime += 1  # Next number to consider
        is_prime = True

        visited_nodes.append(5) # Check Condition of for loop
        for i in range(num_primes):  # For each previous prime
            visited_nodes.append(6) # Check Condition of if statement
            if is_divisible(primes[i], cur_prime):  # Found a divisor, cur_prime is not prime
                visited_nodes.append(7) # Execution of if statement
                is_prime = False
                break  # Out of loop through primes
            visited_nodes.append(5) # Check condition of for loop

        visited_nodes.append(8) # Check Condition of if statement
        if is_prime:  # Save it
            visited_nodes.append(9) # Execution of if statement
            primes[num_primes] = cur_prime
            num_primes += 1

        visited_nodes.append(3) # Check Condition of while loop

    # Print all the primes out
    visited_nodes.append(10) # Execution of for loop
    for i in range(num_primes):
        visited_nodes.append(11)
        print(f"Prime: {primes[i]}")
        visited_nodes.append(10) # Check Condition of for loop
        
    visited_nodes.append(12) # End of function
    print(f"Visited Nodes: {visited_nodes}\n")

def create_cfg():
    """
    Generates a Control Flow Graph (CFG) for the print_primes function.
    """
    cfg = nx.DiGraph()

    # Nodes representing different parts of the program
    cfg.add_nodes_from([
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"
    ])

    # Edges representing control flow
    edges = [
        ("1", "2"),     # Start -> Initialization
        ("2", "3"),     # Initialization -> Check while loop condition
        ("3", "4"),     # while loop condition is true
        ("3", "10"),    # while loop condition is false
        ("4", "5"),     # Execution of while loop -> Check for loop condition
        ("5", "6"),     # for loop condition is true
        ("5", "8"),     # for loop condition is false
        ("6", "5"),     # is not divisible -> Check for loop condition
        ("6", "7"),     # is divisible
        ("7", "5"),     # Loop back to check for loop condition
        ("8", "9"),     # is prime
        ("8", "3"),     # is not prime
        ("9", "3"),     # Loop back to check while loop condition
        ("10", "11"),   # Execution of for loop -> Print primes
        ("11", "10"),   # Loop back to check for loop condition
        ("10", "12")    # End of function
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
        ("3", "4"): "while loop condition is true",
        ("3", "10"):"while loop condition is false",
        ("5", "8"): "for loop condition is false",
        ("6", "5"): "is not divisible",
        ("6", "7"): "is divisible",
        ("8", "9"): "is prime",
        ("8", "3"): "is not prime",
        ("10", "11"): "Execution of for loop",
        ("10", "12"): "End of function"
    }
    
    # Draw edge labels
    nx.draw_networkx_edge_labels(cfg, pos, edge_labels=edge_labels, font_color='red')
    
    plt.title("Control Flow Graph of print_primes Function")
    plt.show()

# Example usage
print_primes(1)

# Generate and display CFG
cfg = create_cfg()
draw_cfg(cfg)