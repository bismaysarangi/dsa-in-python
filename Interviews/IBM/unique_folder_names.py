def unique_folders(n, names):
    count = {}
    result = []
    for name in names:
        if name not in count:
            result.append(name)
            count[name] = 1
        else:
            result.append(f"{name}{count[name]}")
            count[name] += 1
    return result

n = int(input())
names = []
for _ in range(n):
    names.append(input())

print(unique_folders(n, names))