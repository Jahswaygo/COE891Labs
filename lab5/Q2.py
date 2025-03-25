import networkx as nx
import matplotlib.pyplot as plt

# Define the control flow graph (CFG) for the given program
# Simulate the program execution and track visited nodes
def simulate_program(y):
    visited_nodes = []
    visited_nodes.append("Start")  # Start of the program

    # Node 1: int x = y;
    visited_nodes.append("1")
    x = y

    # Node 2: check while condition (x < 100)
    visited_nodes.append("2")
    while x < 100:
        # Node 3: Enter While loop
        visited_nodes.append("3")
        if x < y:
            # Node 4: x <  y is true
            visited_nodes.append("4")
            x += 1
            break
        
        # Node 5: Check for loop condition (int z = 1; z < x; z++)
        visited_nodes.append("5")
        for z in range(1, x):
            # Node 6: for loop
            visited_nodes.append("6")
            x += z
            # Node 5 (Loop back): Check for loop condition (int z = 1; z < x; z++)
            visited_nodes.append("5")

        # Node 7:check if condition (x > 5)
        visited_nodes.append("7")
        if x > 5:
            # Node 8: x > 5 is true
            visited_nodes.append("8")
            y += 1
        else:
            # Node 9: x > 5 is false
            visited_nodes.append("9")
            y += 2

        # Node 2: check while condition (x < 100)
        visited_nodes.append("2")
        
    # Node 12: System.out.println(x + ',' + y);
    visited_nodes.append("10")
    print(f"{x}, {y}")

    # End of the program
    visited_nodes.append("End")
    print(f"Visited Nodes: {visited_nodes}")
    return visited_nodes

def create_cfg():
    """
    Generates a simplified Control Flow Graph (CFG) for the power function.
    """
    cfg = nx.DiGraph()

    # Nodes representing different parts of the program
    cfg.add_nodes_from([
        "Start","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "End"
    ])

    # Edges representing control flow
    edges = [
        ("Start","1"),
        ("1", "2"),
        ("2", "3"),  # while true
        ("2", "10"),  # while false
        ("3", "4"),  # if true
        ("3", "5"),  # if false
        ("4", "10"), # break  
        ("5", "6"),  # for loop true
        ("5", "7"),  # for loop false
        ("6", "5"),  # Loop back
        ("7", "8"),  # if true
        ("7", "9"),  # if false
        ("8", "2"),  # Loop back
        ("9", "2"),  # Loop back
        ("10", "End")
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
        ("2", "10"): "while false",
        ("3", "4"): "if true",
        ("3", "5"): "if false",
        ("5", "6"): "for loop true",
        ("5", "7"): "for loop false",
        ("7", "8"): "if true",
        ("7", "9"): "if false"
    }
    
    # Draw edge labels
    nx.draw_networkx_edge_labels(cfg, pos, edge_labels=edge_labels, font_color='red')
    
    plt.title("Control Flow Graph")
    plt.show()

# Main function to print necessary outputs
if __name__ == "__main__":
    draw_cfg(create_cfg())  # Draw the CFG for the program
    simulate_program(1)  # Simulate the program execution with y=1
