def two_sum(n, target, A):
    seen = {}
    for i in range(n):
        complement = target - A[i]
        if complement in seen:
            return [seen[complement], i]
        seen[A[i]] = i
    return []

n = int(input())
target = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

print(two_sum(n, target, A))