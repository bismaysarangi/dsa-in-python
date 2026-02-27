def run_length(s):
    tot_sum = 0
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count % 2 == 0:
                tot_sum += count
            count = 1
    
    if count % 2 == 0:
        tot_sum += count
    
    return tot_sum

s = input("Enter string: ")
print("Output:", run_length(s))