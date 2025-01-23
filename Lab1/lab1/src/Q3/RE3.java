package Q3;

import java.util.*;

public class RE3 {
    public static boolean checkPhoneNumber(String s) {
        // 5. Corrected regular expression to allow white space anywhere except between
        // adjacent number characters
        // \s* matches any whitespace character (space, tab, newline) zero or more times
        // (\d\s*){3} matches a digit followed by zero or more whitespace characters,
        // exactly three times
        // \s*-\s* matches any whitespace character zero or more times followed by any
        // whitespace character zero or more times
        return s.matches("\\s*\\(\\s*(\\d\\s*){3}\\s*\\)\\s*(\\d\\s*){3}\\s*-\\s*(\\d\\s*){4}\\s*");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a phone number: ");
        String input = sc.nextLine();
        boolean wasPhoneNum = checkPhoneNumber(input);
        System.out.println("\nThat was" + (wasPhoneNum ? "" : "n't") + " a phone number.");
    }
}