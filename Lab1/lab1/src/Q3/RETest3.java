package Q3;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Test;

public class RETest3 {
    @Test
    public void testValidPhoneNumber1() {
        // Test valid phone number with no space after area code
        assertTrue(RE3.checkPhoneNumber("(123)123 - 1234"));
    }

    @Test
    public void testValidPhoneNumber2() {
        // Test valid phone number with space after area code
        assertTrue(RE3.checkPhoneNumber("(123) 456 - 7890"));
    }

    @Test
    public void testInvalidPhoneNumber1() {
        // Test invalid phone number without parentheses
        assertFalse(RE3.checkPhoneNumber("123 123 - 1234"));
    }

    @Test
    public void testInvalidPhoneNumber2() {
        // Test invalid phone number with letters
        assertFalse(RE3.checkPhoneNumber("(123) ABC - 1234"));
    }

    @Test
    public void testValidPhoneNumber3() {
        // Test valid phone number with multiple spaces
        assertTrue(RE3.checkPhoneNumber("( 123 )  456  -  7890"));
    }
}
