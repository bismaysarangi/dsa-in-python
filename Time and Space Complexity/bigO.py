def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)  #O(n**2)



print_items(10) 

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

print(sum(100)) #Recursive way to find sum of all numbers upto n