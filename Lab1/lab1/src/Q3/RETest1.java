package Q3;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Test;

// 3. All Tests Fail because pattern does not account for the parenthesis
public class RETest1 {
    @Test
    public void testValidPhoneNumber1() {
        // Test valid phone number with no space after area code
        assertTrue(RE.checkPhoneNumber("(123)123 - 1234"));
    }

    @Test
    public void testValidPhoneNumber2() {
        // Test valid phone number with space after area code
        assertTrue(RE.checkPhoneNumber("(123) 456 - 7890"));
    }

    @Test
    public void testInvalidPhoneNumber() {
        // Test invalid phone number without parentheses
        assertFalse(RE.checkPhoneNumber("123 123 - 1234"));
    }
}
