package Q5;

public class Fibonacci {
    public static int compute(int n) {
        int result = 0;
        // Base case: if n is 0 or 1, return n
        if (n <= 1) {
            result = n;
        } else {
            // Recursive case: compute the sum of the two preceding numbers
            result = compute(n - 1) + compute(n - 2);
        }
        return result;
    }
}
