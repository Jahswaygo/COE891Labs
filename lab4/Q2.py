import networkx as nx
import matplotlib.pyplot as plt

def is_palindrome(s):
    """
    Checks if the given string is a palindrome.
    """
    visited_nodes = []
    
    visited_nodes.append("1") #Start
    visited_nodes.append("2") #if s is None
    if s is None:
        visited_nodes.append("3") #throw NullPointerException
        raise NullPointerException(f"Visited Nodes: {visited_nodes}\n")
    else:
        visited_nodes.append("4")
        left = 0
        right = len(s) - 1
        result = True
        
        visited_nodes.append("5") #while loop
        while left < right and result:
            visited_nodes.append("6") #in while loop, executing if condition
            if s[left] != s[right]:
                visited_nodes.append("7") #if condition is true
                result = False
            
            visited_nodes.append("8") #left and right are decremented
            left += 1
            right -= 1
            
            visited_nodes.append("5") # Check the while loop condition again
        
        
        visited_nodes.append("9") #return result
    print(f"Visited Nodes: {visited_nodes}\n")
    
    return result

class NullPointerException(Exception):
    pass

def create_cfg():
    """
    Generates a Control Flow Graph (CFG) for the is_palindrome function.
    """
    cfg = nx.DiGraph()

    # Nodes representing different parts of the program
    cfg.add_nodes_from([
        "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ])

    # Edges representing control flow
    edges = [
        ("1", "2"),
        ("2", "3"),  # if s is None
        ("2", "4"),  # else
        ("4", "5"),
        ("5", "6"),  # while true
        ("5", "9"),   # while false
        ("6", "7"),  # if true
        ("6", "8"),  # if false
        ("7", "8"),
        ("8", "5")  # loop back
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
        ("2", "3"): "if s is None",
        ("2", "4"): "else",
        ("5", "6"): "while true",
        ("6", "7"): "if true",
        ("6", "8"): "if false",
        ("8", "5"): "loop back",
        ("5", "9"): "while false"
    }
    
    # Draw edge labels
    nx.draw_networkx_edge_labels(cfg, pos, edge_labels=edge_labels, font_color='red')
    
    plt.title("Control Flow Graph of is_palindrome Function")
    plt.show()

def node_coverage_test_cases():
    # Test cases for node coverage
    test_cases = [
        {'s': None},        # throws NullPointerException
        {'s': "hello"}      # not a palindrome
        
    ]
    return test_cases

def edge_coverage_test_cases():
    # Test cases for edge coverage
    test_cases = [
        {'s': "racecar"},   # palindrome
        {'s': "he"},     # not a palindrome
        {'s': None}         # throws NullPointerException
    ]
    return test_cases

def edge_pair_coverage_test_cases():
    # Test cases for edge-pair coverage
    test_cases = [
        {'s': "racecar"},   # palindrome
        {'s': "abfhba"},  # not a palindrome
        {'s': "aa"},        # even length palindrome
        {'s': "ba"},        # even length not a palindrome
        {'s': None},         # throws NullPointerException
        {'s': "G"},         # single letter palindrome
    ]
    return test_cases

def prime_path_coverage_test_cases():
    # Test cases for prime path coverage
    test_cases = [
        {'s': "racecar"},   # palindrome
        {'s': "abcxba"},    # even long length not a palindrome
        {'s': None},        # throws NullPointerException
        {'s': "G"},         # single letter palindrome
        {'s': "ba"}         # even length not a palindrome
    ]
    return test_cases

def run_test_cases(test_cases):
    for test in test_cases:
        print(f"Test case: {test}")
        try:
            is_palindrome(test['s'])
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    # Generate and display CFG
    cfg = create_cfg()
    draw_cfg(cfg)
    
    # Provide test cases for node coverage
    print("\nNode Coverage Test Cases:", node_coverage_test_cases())
    run_test_cases(node_coverage_test_cases())
    
    
    # Provide test cases for edge coverage
    print("\nEdge Coverage Test Cases:", edge_coverage_test_cases())
    run_test_cases(edge_coverage_test_cases())

    # Provide test cases for edge-pair coverage
    print("\nEdge-Pair Coverage Test Cases:", edge_pair_coverage_test_cases())
    run_test_cases(edge_pair_coverage_test_cases())

    # Provide test cases for prime path coverage
    print("\nPrime Path Coverage Test Cases:", prime_path_coverage_test_cases())
    run_test_cases(prime_path_coverage_test_cases())
