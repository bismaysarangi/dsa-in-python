myDict = {'name': 'Jack', 'age': 26}

def traverseDict(myDict):
    for key in myDict:
        print(key, dict[key])

traverseDict(myDict)

#Linear Search
def searchDict(myDict, value):
    for key in myDict:
        if myDict[key] == value:
            return key, value
    return "The value does not exist in the dictionary"

print(searchDict(myDict, 26))