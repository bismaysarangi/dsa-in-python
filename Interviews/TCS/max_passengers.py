def max_passengers(n, arr):
    max_p = 0
    current = 0

    for i in range(n):
        current -= arr[i][0] 
        current += arr[i][1]  
        max_p = max(max_p, current)
    
    return max_p

n = int(input())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

print(max_passengers(n, arr))