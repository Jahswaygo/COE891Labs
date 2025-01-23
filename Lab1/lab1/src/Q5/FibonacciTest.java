package Q5;

import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.Collection;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@RunWith(Parameterized.class)
public class FibonacciTest {
    private int input;
    private int expected;

    // Constructor to initialize the test case with input and expected output
    public FibonacciTest(int input, int expected) {
        this.input = input;
        this.expected = expected;
    }

    // Define the parameters for the test cases
    @Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][] {
                // Test cases with input and expected output
                { 0, 0 },
                { 1, 1 },
                { 2, 1 },
                { 3, 2 },
                { 4, 3 },
                { 5, 5 },
                { 6, 8 },
                { 7, 13 },
                { 8, 21 },
                { 9, 34 }
        });
    }

    // Test method to verify the Fibonacci computation
    @Test
    public void testFibonacci() {
        assertEquals(expected, Fibonacci.compute(input));
    }
}
