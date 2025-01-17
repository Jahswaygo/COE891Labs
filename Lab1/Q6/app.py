class PrimeNumberChecker:
    @staticmethod
    def is_prime(n: int) -> bool:
        # Check if the number is less than or equal to 1
        if n <= 1:
            return False
        # Check for factors from 2 to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        # If no factors are found, the number is prime
        return True

if __name__ == "__main__":
    # Example usage
    numbers = [2, 6, 19, 22, 23]
    for number in numbers:
        # Print whether each number is prime or not
        print(f"{number} is {'a prime number' if PrimeNumberChecker.is_prime(number) else 'not a prime number'}")
