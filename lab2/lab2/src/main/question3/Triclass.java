package question3;

public class Triclass {
    public static String classify(int x, int y, int z) {
        // Check for invalid triangles
        if (x <= 0 || y <= 0 || z <= 0) {
            return "not a triangle";
        }
        if (x + y <= z || x + z <= y || y + z <= x) {
            return "not a triangle";
        }

        // Classification logic
        if (x == y && y == z) {
            return "equilateral";
        } else if (x == y || y == z || x == z) {
            return "isosceles";
        } else {
            return "scalene";
        }
    }
}