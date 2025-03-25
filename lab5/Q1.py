from itertools import product

# Predicate: p = a ∧ (∼ b ∨ c)
def evaluate_predicate(a, b, c):
    return a and (not b or c)

# Generate truth table for all combinations of (a, b, c)
def generate_truth_table():
    return [(a, b, c, evaluate_predicate(a, b, c)) for a, b, c in product([False, True], repeat=3)]

# Print the truth table
def print_truth_table():
    truth_table = generate_truth_table()
    print("Truth Table:")
    print("a      | b     | c       | p")
    print("--------------------------")
    for row in truth_table:
        print(f"{row[0]:<6} | {row[1]:<6} | {row[2]:<6} | {row[3]}")

# Call the function to print the truth table
if __name__ == "__main__":
    print_truth_table()