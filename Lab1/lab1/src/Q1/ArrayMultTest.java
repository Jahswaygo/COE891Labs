package Q1;

import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

public class ArrayMultTest {

    @Test
    public void testMultSameLength() {
        ArrayMult arrayMult = new ArrayMult();
        int[] array1 = { 1, 2, 3 };
        int[] array2 = { 4, 5, 6 };
        int[] expected = { 4, 10, 18 };
        // Test case where both arrays have the same length
        assertArrayEquals(expected, arrayMult.mult(array1, array2));
    }

    @Test
    public void testMultDifferentLength() {
        ArrayMult arrayMult = new ArrayMult();
        int[] array1 = { 1, 2 };
        int[] array2 = { 3, 4, 5 };
        int[] expected = { 3, 8, 5 };
        // Test case where the second array is longer
        assertArrayEquals(expected, arrayMult.mult(array1, array2));
    }

    @Test
    public void testMultFirstArrayLonger() {
        ArrayMult arrayMult = new ArrayMult();
        int[] array1 = { 1, 2, 3, 4 };
        int[] array2 = { 5, 6 };
        int[] expected = { 5, 12, 3, 4 };
        // Test case where the first array is longer
        assertArrayEquals(expected, arrayMult.mult(array1, array2));
    }

    @Test
    public void testMultSecondArrayLonger() {
        ArrayMult arrayMult = new ArrayMult();
        int[] array1 = { 7, 8 };
        int[] array2 = { 9, 10, 11, 12 };
        int[] expected = { 63, 80, 11, 12 };
        // Test case where the second array is longer
        assertArrayEquals(expected, arrayMult.mult(array1, array2));
    }
}
