package Q3;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class RETest2 {
    @Test // 4. Fails due to the lack of space between area code and following numbers
    public void testValidPhoneNumber1() {
        // Test valid phone number with no space after area code
        assertTrue(RE2.checkPhoneNumber("(123)123 - 1234"));
    }
    // 3. ^^Fails because it needs a space after even with a parenthesis

    @Test
    public void testValidPhoneNumber2() {
        // Test valid phone number with space after area code
        assertTrue(RE2.checkPhoneNumber("(123) 456 - 7890"));
    }
}
