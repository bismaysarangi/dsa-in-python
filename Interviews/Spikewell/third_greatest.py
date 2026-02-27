def thirdGreatest(strArr):
    lengths = [len(word) for word in strArr]
    lengths.sort()

    third_greatest_length = lengths[-3]
    for word in reversed(strArr):
        if len(word) == third_greatest_length:
            return word
        
# Example usage:
print(thirdGreatest(["coder", "byte", "code"]))  # Output: "code"
print(thirdGreatest(["abc", "defg", "z", "hijk"]))  # Output: "abc"
print(thirdGreatest(["hello", "world", "before", "all"]))  # Expected: "world"
print(thirdGreatest(["hello", "world", "after", "all"]))  # Expected: "after"
print(thirdGreatest(["coder", "byte", "code"]))  # Expected: "code"
print(thirdGreatest(["abc", "defg", "z", "hijk"]))  # Expected: "abc"