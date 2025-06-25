# Common Keys
# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:

# {'a': 1, 'b': 5, 'c': 7, 'd': 5}

from collections import Counter
def merge_dicts(dict1, dict2):
    # TODO
    c1 = Counter(dict1)
    c2 = Counter(dict2)
    
    merged_counter = c1 + c2
    return dict(merged_counter)
    
