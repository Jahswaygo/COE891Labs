package Q3;

import java.util.*;

public class RE {
    public static boolean checkPhoneNumber(String s) {
        // 1. Corrected regular expression with proper escaping
        return s.matches("(\\d{3}) \\d{3} - \\d{4}");
    }

    /*
     * 2.
     * In Java, `\d` is a metacharacter used in regular expressions to match any
     * digit (0-9).
     * When creating a string in Java, you need to escape the backslash with another
     * backslash, so `\d` becomes `\\d`. This is because the backslash is an escape
     * character in Java strings.
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a phone number: ");
        String input = sc.nextLine();
        boolean wasPhoneNum = checkPhoneNumber(input);
        System.out.println("\nThat was" + (wasPhoneNum ? "" : "n't") + " a phone number.");
    }
}