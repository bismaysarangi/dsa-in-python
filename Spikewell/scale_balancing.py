def scale_balancing(strArr):
    # Parse input
    scale = eval(strArr[0])  # e.g., [5, 9]
    weights = eval(strArr[1])  # e.g., [1, 2, 6, 7]
    
    left, right = scale[0], scale[1]
    diff = abs(left - right)
    
    heavier_side = "left" if left > right else "right"

    # If already balanced
    if diff == 0:
        return "not possible"
    
    # Try using just 1 weight
    for w in weights:
        if w == diff:
            return str(w)
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
                return f"{min(w1, w2)}, {max(w1, w2)}"
            # Case 2: Both weights on the heavier side
            if heavier_side == "left":
                if right + w1 + w2 == left:
                    return f"{min(w1, w2)}, {max(w1, w2)}"
            else:
                if left + w1 + w2 == right:
                    return f"{min(w1, w2)}, {max(w1, w2)}"
            # Case 3: One weight on each side
            if heavier_side == "left":
                if right + w1 == left + w2:
                    return f"{min(w1, w2)}, {max(w1, w2)}"
                if right + w2 == left + w1:
                    return f"{min(w1, w2)}, {max(w1, w2)}"
            else:
                if left + w1 == right + w2:
                    return f"{min(w1, w2)}, {max(w1, w2)}"
                if left + w2 == right + w1:
                    return f"{min(w1, w2)}, {max(w1, w2)}"
    return "not possible"



# Example Usage:
print(scale_balancing(["[5, 9]", "[1, 2, 6, 7]"]))  # Expected: "2,6"
print(scale_balancing(["[3, 4]", "[1, 2, 7, 7]"]))  # Expected: "1"