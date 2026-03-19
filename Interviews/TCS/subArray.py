def sub_array(arr, n, target):
    for i in range(n):
        curr = 0
        for j in range(i, n):
            curr += arr[j]
            if curr == target:
                print(arr[i:j+1])


n = input()
n = int(n)
target = input()
target = int(target)
arr = []

for _ in range(n):
    arr.append(int(input()))
# arr = list(map(int, input().split()))

sub_array(arr, n, target)