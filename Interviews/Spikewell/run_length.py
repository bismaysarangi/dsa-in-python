# Run Length
def run_length(string):
    if not string:
        return ""
    result = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result.append(f"{count}{string[i - 1]}")
            count = 1
    
    result.append(f"{count}{string[-1]}")
    return "".join(result)

# Example usage:
print("Using manual approach:")
print(run_length("aabbcde"))  # Expected: "2a2b1c1d1e"
print(run_length("wwwbbbw"))  # Expected: "3w3b1w"
print(run_length("wwwggopp"))  # Expected: "3w2g1o2p"
print(run_length("aaaa"))  # Expected: "4a"
print(run_length("a"))