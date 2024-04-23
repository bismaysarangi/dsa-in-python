# my_array = ['1', '2', '3']

def traversal(my_array):
    for i in my_array:
        print(i, end = " ")
    print()

def access_element(array, index):
    if index > len(array):
        print("There is no element in this index")
    else:
        print(array[index])


traversal(['1', '2', '3'])

access_element(['1', '2', '3'], -1)
