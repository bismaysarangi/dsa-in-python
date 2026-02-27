def third_greatest(n, s):
    lengths = [len(word) for word in s]
    lengths.sort()

    third_greatest_length = lengths[-3]
    for word in reversed(s):
        if len(word) == third_greatest_length:
            return word

n = int(input())
s = []
for _ in range(n):
    s.append(input())

print(third_greatest(n, s))