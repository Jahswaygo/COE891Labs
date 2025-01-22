import re  # Import the regular expression module

class RE:
    @staticmethod
    def check_phone_number(s: str) -> bool:
        #5. Revisede expression to check if the phone number matches the pattern
        # - \s? matches zero or one whitespace character
        # The pattern \(\d{3}\)\s?\d{3}\s?-\s?\d{4} matches:
        # - \( and \) match the literal parentheses
        # - \d{3} matches exactly three digits
        # - \s? matches zero or one whitespace character
        # - \d{3} matches exactly three digits
        # - \s? matches zero or one whitespace character
        # - - matches the literal hyphen
        # - \s? matches zero or one whitespace character
        # - \d{4} matches exactly four digits
        return bool(re.match(r"\(\d{3}\)\s?\d{3}\s?-\s?\d{4}", s))

if __name__ == "__main__":
    # Prompt the user to enter a phone number
    input_phone_number = input("Enter a phone number: ")
    # Check if the entered phone number is valid
    was_phone_num = RE.check_phone_number(input_phone_number)
    # Print the result
    print(f"\nThat was{'' if was_phone_num else "n't"} a phone number.")

