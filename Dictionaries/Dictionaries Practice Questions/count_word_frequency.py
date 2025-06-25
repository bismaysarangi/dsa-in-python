# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# count_word_frequency(words) 
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}

from collections import Counter
def count_word_frequency(words):
    # TODO
    res = Counter(words)
    sorted_res = sorted(res.items())
    sorted_res.sort(key = lambda x:x[1], reverse = True)
    
    return dict(sorted_res)