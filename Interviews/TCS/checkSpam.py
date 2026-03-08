def check_spam(s):
    if len(s) < 3:
        return "NOT SPAM"
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return "SPAM"
    return "NOT SPAM"


s = input("Enter the string: ")
print(check_spam(s))