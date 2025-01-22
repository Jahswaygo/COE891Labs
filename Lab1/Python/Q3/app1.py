import re  # Import the regular expression module

class RE:
    @staticmethod
    def check_phone_number(s: str) -> bool:
        # Use a regular expression to check if the phone number matches the pattern
        # The pattern \(\d{3}\)\d{3}-\d{4} matches:
        # - \( and \) match the literal parentheses
        # - \d{3} matches exactly three digits
        # - \d{3} matches exactly three digits
        # - - matches the literal hyphen
        # - \d{4} matches exactly four digits
        return bool(re.match(r"\(\d{3}\) \d{3} - \d{4}", s))

if __name__ == "__main__":
    # Prompt the user to enter a phone number
    input_phone_number = input("Enter a phone number: ")
    # Check if the entered phone number is valid
    was_phone_num = RE.check_phone_number(input_phone_number)
    # Print the result
    print(f"\nThat was{'' if was_phone_num else "n't"} a phone number.")

#2.   In Java, `\d` is a shorthand character class in regular expressions that matches any digit (equivalent to `[0-9]`).  
#    When creating a string in Java that includes `\d`, you need to escape the backslash by using a double backslash (`\\d`).
#    This is because the backslash is an escape character in Java strings. "\\d" will match any digit.
#    In Python, `\d` is also a shorthand character class in regular expressions that matches any digit (equivalent to `[0-9]`). 
#    When using `\d` in a regular expression pattern, you do not need to escape the backslash within the pattern string itself.
