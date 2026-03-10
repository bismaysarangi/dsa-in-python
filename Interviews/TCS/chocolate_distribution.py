def chocolate_distribution(n, packets, m):
    packets.sort()
    min_diff = float('inf')

    for i in range(n - m + 1):
        min_diff = min(min_diff, packets[i + m - 1] - packets[i])

    return min_diff


n = input()
n = int(n)

packets = []
for _ in range(n):
    packets.append(int(input()))

m = input()
m = int(m)

print(chocolate_distribution(n, packets, m))