def array_hitting(n, k, arr):
    count = 0
    for i in range(n):
        if arr[i] - k > k:
            count += 1
    return count    

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(array_hitting(n, k, arr))