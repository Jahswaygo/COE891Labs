package Q8;

import static org.junit.Assert.assertEquals;
import org.junit.experimental.theories.DataPoint;
import org.junit.experimental.theories.Theories;
import org.junit.experimental.theories.Theory;
import org.junit.runner.RunWith;
import Q6.PNC;

// Use the Theories runner to run the test with multiple sets of parameters
@RunWith(Theories.class)
public class PNCTheoryTest {
    // Create an instance of the PNC class to test its methods
    private PNC PNC = new PNC();

    // Define data points for the test cases
    @DataPoint
    public static int[] primeCase1 = { 2, 1 }; // 2 is prime
    @DataPoint
    public static int[] nonPrimeCase1 = { 6, 0 }; // 6 is not prime
    @DataPoint
    public static int[] primeCase2 = { 19, 1 }; // 19 is prime
    @DataPoint
    public static int[] nonPrimeCase2 = { 22, 0 }; // 22 is not prime
    @DataPoint
    public static int[] primeCase3 = { 23, 1 }; // 23 is prime

    // Theory to test the isPrime method with different test cases
    @Theory
    public void testPNC(int[] testCase) {
        // Extract the input number and the expected result from the test case
        int inputNumber = testCase[0];
        boolean expectedResult = testCase[1] == 1;
        // Assert that the result of isPrime matches the expected result
        assertEquals(expectedResult, PNC.isPrime(inputNumber));
    }
}
