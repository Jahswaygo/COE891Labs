package Q8;

import static org.junit.Assert.assertEquals;
import org.junit.experimental.theories.DataPoint;
import org.junit.experimental.theories.Theories;
import org.junit.experimental.theories.Theory;
import org.junit.runner.RunWith;
import Q5.Fibonacci;

// Use the Theories runner to run the test with multiple sets of parameters
@RunWith(Theories.class)
public class FibTheoryTest {
    // Define data points for the test cases
    @DataPoint
    public static int[] fibCase1 = { 0, 0 }; // Fibonacci(0) = 0
    @DataPoint
    public static int[] fibCase2 = { 1, 1 }; // Fibonacci(1) = 1
    @DataPoint
    public static int[] fibCase3 = { 2, 1 }; // Fibonacci(2) = 1
    @DataPoint
    public static int[] fibCase4 = { 3, 2 }; // Fibonacci(3) = 2
    @DataPoint
    public static int[] fibCase5 = { 4, 3 }; // Fibonacci(4) = 3
    @DataPoint
    public static int[] fibCase6 = { 5, 5 }; // Fibonacci(5) = 5
    @DataPoint
    public static int[] fibCase7 = { 6, 8 }; // Fibonacci(6) = 8

    // Theory to test the fibonacci method with different test cases
    @Theory
    public void testFibonacci(int[] testCase) {
        // Extract the input number and the expected result from the test case
        int inputNumber = testCase[0];
        int expectedResult = testCase[1];
        // Assert that the result of fibonacci matches the expected result
        assertEquals(expectedResult, Fibonacci.compute(inputNumber));
    }
}
