newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple[1:3])  # ('b', 'c')  

newT = tuple('abcde')
print(newT[1:])  # ('b', 'c')

#Traversal
for i in newT:
    print(i, end=' ')  # a b c d e
print("\n")
#Search an element in tuple
print('a' in newT)  # True
print(newT.index('a'))  # 0

#Count the number of elements in tuple      
print(newT.count('a'))  # 1

#Concatenation  
newT1 = newT + newTuple
print(newT1)  # ('a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e')

#Repetition
newT2 = newT * 2
print(newT2)  # ('a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e')

#Slicing
print(newT[1:3])  # ('b', 'c')

#Length
print(len(newT))  # 5

#Minimum
print(min(newT))  # a

#Maximum    
print(max(newT))  # e

#Convert list to tuple
newList = ['a', 'b', 'c', 'd', 'e']
newTuple = tuple(newList)
print(newTuple)  # ('a', 'b', 'c', 'd', 'e')

#Convert tuple to list
newList = list(newTuple)
print(newList)  # ['a', 'b', 'c', 'd', 'e']

#Convert string to tuple
newTuple = tuple('abcde')
print(newTuple)  # ('a', 'b', 'c', 'd', 'e')

#Convert tuple to string
newString = ''.join(newTuple)
print(newString)  # abcde

#Convert tuple to dictionary
newTuple = (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5))
newDict = dict(newTuple)
print(newDict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

#Convert dictionary to tuple
newDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
newTuple = tuple(newDict.items())
print(newTuple)  # (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5))

#Convert tuple to set   
newTuple = ('a', 'b', 'c', 'd', 'e')
newSet = set(newTuple)
print(newSet)  # {'a', 'b', 'c', 'd', 'e'}

#Convert set to tuple
newSet = {'a', 'b', 'c', 'd', 'e'}
newTuple = tuple(newSet)
print(newTuple)  # ('a', 'b', 'c', 'd', 'e')
