# Array Balance
"""
CODERBYTE SCALE BALANCING CHALLENGE

Problem: Balance a scale using at most 2 weights from a given list.
- Input: Two strings - current weights "[left, right]" and available weights "[w1, w2, ...]"
- Output: Comma-separated weights used (ascending order) or "not possible"

Examples:
- Input: ["[5, 9]", "[1, 2, 6, 7]"] → Output: "2,6"
- Input: ["[3, 4]", "[1, 2, 7, 7]"] → Output: "1"
- Input: ["[13, 4]", "[1, 2, 3, 6, 14]"] → Output: "3,6"
"""

def scale_balancing(str_arr):
    # Parse input
    left, right = map(int, str_arr[0].strip("[]").split(","))
    weights = list(map(int, str_arr[1].strip("[]").split(",")))
    
    # Calculate the difference (how much heavier one side is)
    diff = abs(left - right)
    heavier_side = "left" if left > right else "right"
    
    # If already balanced
    if diff == 0:
        return "not possible"
    
    # Try using just 1 weight
    for w in weights:
        # Add weight to lighter side
        if w == diff:
            return str(w)
        # Add weight to heavier side (needs to make opposite side heavier)
        # This handles cases where adding to heavier side creates new balance
        if heavier_side == "left":
            if right + w == left:
                return str(w)
        else:
            if left + w == right:
                return str(w)
    
    # Try using 2 weights
    for i in range(len(weights)):
        for j in range(i + 1, len(weights)):
            w1, w2 = weights[i], weights[j]
            
            # Case 1: Both weights on the lighter side
            if w1 + w2 == diff:
                return f"{min(w1, w2)},{max(w1, w2)}"
            
            # Case 2: Both weights on the heavier side
            if heavier_side == "left":
                if right + w1 + w2 == left:
                    return f"{min(w1, w2)},{max(w1, w2)}"
            else:
                if left + w1 + w2 == right:
                    return f"{min(w1, w2)},{max(w1, w2)}"
            
            # Case 3: One weight on each side
            # w1 on lighter, w2 on heavier
            if heavier_side == "left":
                if right + w1 == left + w2:
                    return f"{min(w1, w2)},{max(w1, w2)}"
                if right + w2 == left + w1:
                    return f"{min(w1, w2)},{max(w1, w2)}"
            else:
                if left + w1 == right + w2:
                    return f"{min(w1, w2)},{max(w1, w2)}"
                if left + w2 == right + w1:
                    return f"{min(w1, w2)},{max(w1, w2)}"
    
    return "not possible"


# Test cases
if __name__ == "__main__":
    # Test 1
    print(scale_balancing(["[5, 9]", "[1, 2, 6, 7]"]))  # Expected: "2,6"
    
    # Test 2
    print(scale_balancing(["[3, 4]", "[1, 2, 7, 7]"]))  # Expected: "1"
    
    # Test 3
    print(scale_balancing(["[13, 4]", "[1, 2, 3, 6, 14]"]))  # Expected: "3,6"