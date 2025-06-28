def selectionSort(cList):
    for i in range(len(cList)):
        min_index = i
        for j in range(i + 1, len(cList)):
            if cList[min_index] > cList[j]:
                min_index = j
            cList[i], cList[min_index] = cList[min_index], cList[i]
            
    return cList

print(selectionSort([1, 6, 3, 3, 8]))