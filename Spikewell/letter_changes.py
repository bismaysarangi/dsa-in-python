# Letter Changes
def letter_changes(strArr):
    result = []
    vowels = 'aeiou'

    for char in strArr:
        if char.isalpha():
            if char.lower() == 'z':
                next_char = 'a'
            else:
                next_char = chr(ord(char) + 1)
            if next_char in vowels:
                next_char = next_char.upper()
            result.append(next_char)
        else:
            result.append(char)
    return ''.join(result)

# Example usage:
print(letter_changes("hello*3"))  # Expected: "Ifmmp*3"
    
    # Test 2
print(letter_changes("fun times!"))  # Expected: "gvO Ujnft!"
    
    # Additional tests
print(letter_changes("xyz"))  # Expected: "yzA"
print(letter_changes("abc"))  # Expected: "bcd"
print(letter_changes("ZZZ"))  # Expected: "AAA"