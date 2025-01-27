package Q3;

import java.util.*;

public class RE2 {
    public static boolean checkPhoneNumber(String s) {
        return s.matches("\\(\\d{3}\\) \\d{3} - \\d{4}");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a phone number: ");
        String input = sc.nextLine();
        boolean wasPhoneNum = checkPhoneNumber(input);
        System.out.println("\nThat was" + (wasPhoneNum ? "" : "n't") + " a phone number.");
    }
}