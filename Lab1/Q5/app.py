class Fibonacci:
    @staticmethod
    def compute(n: int) -> int:
        # Base case: if n is 0 or 1, return n
        if n <= 1:
            return n
        # Recursive case: compute the sum of the two preceding numbers
        return Fibonacci.compute(n - 1) + Fibonacci.compute(n - 2)

if __name__ == "__main__":
    # Compute and print the first 10 Fibonacci numbers
    for i in range(10):
        print(f"Fibonacci({i}) = {Fibonacci.compute(i)}")
