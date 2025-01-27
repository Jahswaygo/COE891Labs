package Q7;

import static org.junit.Assume.assumeTrue;
import static org.junit.Assert.assertTrue;
import org.junit.experimental.theories.DataPoints;
import org.junit.experimental.theories.Theory;
import org.junit.experimental.theories.Theories;
import org.junit.runner.RunWith;

@RunWith(Theories.class)
public class MTHTheoryTest3 {

    // Define data points for the tests

    @DataPoints
    public static int[] extendedVal = { 0, -1, -10, -1234, 1, 10, 6789, Integer.MAX_VALUE, Integer.MIN_VALUE };

    // Theory to test if the sum of two positive numbers is greater than each of the
    // numbers
    @Theory
    public void testSumGreaterThanEach(int a, int b) {
        // Assume that both a and b are positive
        assumeTrue(a > 0 && b > 0);
        // Debug output
        System.out.println("Testing sumGreaterThanEach with a=" + a + ", b=" + b);
        // Assert that the sum of a and b is greater than each of the numbers
        assertTrue(MTHTheory.sumGreaterThanEach(a, b));
    }

    // Theory to test the commutative property of addition
    @Theory
    public void testCommutativeProperty(int a, int b) {
        // Debug output
        System.out.println("Testing commutativeProperty with a=" + a + ", b=" + b);
        // Assert that a + b is equal to b + a
        assertTrue(MTHTheory.commutativeProperty(a, b));
    }
}