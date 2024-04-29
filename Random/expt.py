elements = [1, 2, 3, 4, 5, 5]
arr = []

def non_repeating_elements_without_set(elements):
    for i in range(len(elements)):
        if i not in elements:
            arr.append(i)
    return arr

print(non_repeating_elements_without_set(elements))

def using_set(elements):
    return list(set(elements))

print(using_set(elements))