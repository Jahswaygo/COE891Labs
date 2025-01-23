package Q7;

public class MTHTheory {
    // Method to check if the sum of two numbers is greater than each of the numbers
    public static boolean sumGreaterThanEach(int a, int b) {
        // Check if the sum of a and b is greater than a and greater than b
        return (a + b > a) && (a + b > b);
    }

    // Method to check the commutative property of addition
    public static boolean commutativeProperty(int a, int b) {
        // Check if a + b is equal to b + a
        return (a + b) == (b + a);
    }
}
