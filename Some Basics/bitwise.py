print(~12)

print(12 & 13)

print(12 | 13)

print(25 & 30)

print(10 >> 2) #Right Shift 2 bits(0s)

print(10 << 2)#Left Shift 2 bits(0s)

res = 0
for i in range(32):
    if (10 >> i) & 1:
        res += 1
print(res)

# Problem: Single Number
def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        
        return answer