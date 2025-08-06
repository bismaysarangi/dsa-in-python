def bubbleSort(customList):
    for i in range(len(customList) - 1, 0, -1):
        for j in range(i):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    return customList

print(bubbleSort([1, 6, 9, 3, 8]))