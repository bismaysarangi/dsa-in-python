def recover_array(n, pref):
    arr = [pref[0]]
    for i in range(1, n):
        arr.append(pref[i] ^ pref[i - 1])
    return arr

n = int(input())
pref = []
for _ in range(n):
    pref.append(int(input()))

print(recover_array(n, pref))