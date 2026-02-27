def run_length(s):
    if not s:
        return ""
    
    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i - 1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return "".join(result)


print(run_length("aabbcde"))  # Expected: "2a2b1c1d1e"
print(run_length("wwwbbbw"))  # Expected: "3w3b1w"
print(run_length("wwwggopp"))  # Expected: "3w2g1o2p"
print(run_length("aaaa"))  # Expected: "4a"
print(run_length("a"))