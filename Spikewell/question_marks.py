# Question Marks
def question_marks(strArr):
    question_count = 0
    prev_digit = None
    found_valid_pair = False

    for char in strArr:
        if char.isdigit():
            current_digit = int(char)
            if prev_digit is not None:
                if current_digit + prev_digit == 10:
                    if question_count != 3:
                        return "false"
                    found_valid_pair = True
            prev_digit = current_digit
            question_count = 0

        elif char == '?':
            question_count += 1
    
    return "true" if found_valid_pair else "false"

# Example usage:
# print(question_marks("arrb6???4xxbl5???eee5"))  # Output: "true"
print(question_marks("acc?7??sss?3rr1??????5"))  # Output: "true"
# print(question_marks("5??aaaaaaaaaaaaaaaaaaa?5?5"))  # Output: "false"
