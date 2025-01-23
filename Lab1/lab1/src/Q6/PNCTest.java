package Q6;

import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.Collection;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

// Use the Parameterized runner to run the test with multiple sets of parameters
@RunWith(Parameterized.class)
public class PNCTest {
    // Fields to hold the input number and the expected result
    private int inputNumber;
    private boolean expectedResult;
    private PNC PNC;

    // Constructor to initialize the test case with input number and expected result
    public PNCTest(int inputNumber, boolean expectedResult) {
        this.inputNumber = inputNumber;
        this.expectedResult = expectedResult;
        this.PNC = new PNC(); // Initialize the PNC instance
    }

    // Define the parameters for the test cases
    @Parameters
    public static Collection<Object[]> primeNumbers() {
        // Return a collection of test cases with input numbers and expected results
        return Arrays.asList(new Object[][] {
                { 2, true }, // 2 is prime
                { 6, false }, // 6 is not prime
                { 19, true }, // 19 is prime
                { 22, false }, // 22 is not prime
                { 23, true } // 23 is prime
        });
    }

    // Test method to verify the isPrime method
    @Test
    public void testPNC() {
        // Assert that the result of isPrime matches the expected result
        assertEquals(expectedResult, PNC.isPrime(inputNumber));
    }
}
