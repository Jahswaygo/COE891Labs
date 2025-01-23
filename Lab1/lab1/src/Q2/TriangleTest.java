package Q2;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Before;
import org.junit.Test;

public class TriangleTest {
    private Triangle t1;
    private Triangle t2;
    private Triangle t3;

    @Before
    public void setUp() {
        // Initialize triangles with given sides
        t1 = new Triangle(3, 4, 5);
        t2 = new Triangle(5, 4, 3);
        t3 = new Triangle(8, 5, 5);
    }

    // Areas
    @Test
    public void testCalculateAreaT1() {
        // Test area calculation for triangle t1
        double area = t1.calculateArea();
        assertTrue(area > 0);
    }

    @Test
    public void testCalculateAreaT2() {
        // Test area calculation for triangle t2
        double area = t2.calculateArea();
        assertTrue(area > 0);
    }

    @Test
    public void testCalculateAreaT3() {
        // Test area calculation for triangle t3
        double area = t3.calculateArea();
        assertTrue(area > 0);
    }

    // Verifying Area
    @Test
    public void testAreaEqualityT1T2() {
        // Verify that the areas of t1 and t2 are the same
        double area1 = t1.calculateArea();
        double area2 = t2.calculateArea();
        assertTrue(area1 == area2);
    }

    @Test
    public void testInvalidTriangle() {
        // Test case for an invalid triangle
        Triangle invalidTriangle = new Triangle(3, 4, 100);
        double area = invalidTriangle.calculateArea();
        assertFalse(area > 0);
    }
}
