myDict = {'name': 'Jack', 'age': 26, 'address' : 'Downtown'}

dict1 = myDict.copy()
print(dict1)

dict1.clear()
print(dict1)

newDict = {}.fromkeys([1, 2, 3], 0)
print(newDict)

print(myDict.get('name'))

print(myDict.items())

print(myDict.keys())

print(newDict.popitem())

print(myDict.setdefault('name1', 'Ram')) 
print(myDict)

myDict.pop('name1', 'Ram')
print(myDict) 

print(myDict.values())

myDict.update({'name': 'Ram'})
print(myDict)

sortedDict = sorted(myDict)
print(sortedDict)