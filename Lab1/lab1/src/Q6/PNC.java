package Q6;

public class PNC {
    // Method to check if a number is prime
    public boolean isPrime(int number) {
        // If the number is less than or equal to 1, it is not prime
        if (number <= 1) {
            return false;
        }
        // Loop from 2 to the square root of the number
        // If the number is divisible by any number in this range, it is not prime
        for (int i = 2; i <= Math.sqrt(number); i++) {
            // Check if the number is divisible by i
            if (number % i == 0) {
                return false; // If divisible, it is not prime
            }
        }
        // If no divisors were found, the number is prime
        return true;
    }
}
