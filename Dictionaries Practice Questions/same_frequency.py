# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# check_same_frequency(list1, list2)
# Output:

# False

from collections import Counter
def check_same_frequency(list1, list2):
    # TODO
    l1 = Counter(list1)
    l2 = Counter(list2)
    
    return l1 == l2
