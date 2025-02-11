package question3;

import junit.framework.TestCase;

public class TriclassTest extends TestCase {
    private static int testNumber = 0;

    /*
     * public static void main(String[] args) {
     * System.out.println("Testing started");
     * junit.textui.TestRunner.run(TriclassTest.class);
     * System.out.println("Testing is finished");
     * }
     */

    protected void setUp() {
        testNumber++;
        System.out.println("#Test_" + testNumber + " - started");
    }

    protected void tearDown() {
        System.out.println("#Test_" + testNumber + " - finished");
    }

    public void testEquilateral() {
        assertEquals("equilateral", Triclass.classify(4, 4, 4));
        assertEquals("equilateral", Triclass.classify(1, 1, 1));
    }

    public void testIsosceles() {
        assertEquals("isosceles", Triclass.classify(5, 5, 1));
        assertEquals("isosceles", Triclass.classify(5, 2, 5));
        assertEquals("isosceles", Triclass.classify(3, 5, 5));
    }

    public void testScalene() {
        assertEquals("scalene", Triclass.classify(4, 5, 6));
        assertEquals("scalene", Triclass.classify(7, 8, 9));
    }

    public void testInvalidTriangle() {
        assertEquals("not a triangle", Triclass.classify(4, 4, 20));
        assertEquals("not a triangle", Triclass.classify(0, 3, 3));
        assertEquals("not a triangle", Triclass.classify(0, 5, 1));
        assertEquals("not a triangle", Triclass.classify(-1, 5, 5));
        assertEquals("not a triangle", Triclass.classify(-1, -1, -1));
    }
}