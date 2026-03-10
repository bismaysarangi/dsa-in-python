def library_fine(n, arr, k):
    fine = 0
    for i in arr:
        if i > k:
            fine += (i - k) * 1
    return fine 

n = input()
n = int(n)
arr = []
for _ in range(n):
    arr.append(int(input()))

k = input()
k = int(k)


print(library_fine(n, arr, k))