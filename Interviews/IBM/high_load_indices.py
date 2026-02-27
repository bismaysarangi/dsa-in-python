def high_load_indices(n, load):
    avg = sum(load) / n
    indices = []

    for i in range(n):
        if load[i] > 2 * avg:
            indices.append(i)
    return indices


n = int(input())
load = []
for _ in range(n):
    load.append(int(input()))

print(high_load_indices(n, load))