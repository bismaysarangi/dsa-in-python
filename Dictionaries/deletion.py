myDict  = {'name': 'Jack', 'age': 26, 'address' : 'Downtown'}

removed_element = myDict.pop('age')
print(removed_element)
print(myDict)

#popitem() method removes the last inserted item
remove = myDict.popitem()
print(remove)