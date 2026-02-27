def max_subarray_sum(n, A):
    max_sum = float('-inf')
    curr = A[0]

    for i in range(1, n):
        curr = max(A[i], curr + A[i])
        max_sum = max(max_sum, curr)
    return max_sum

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

print(max_subarray_sum(n, A))