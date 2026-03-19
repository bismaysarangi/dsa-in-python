from collections import Counter

def majority_element(s):
    count = Counter(s)
    for key in count:
        if count[key] > len(s) // 2:
            return key
    return None 
s = input()
print(majority_element(s))