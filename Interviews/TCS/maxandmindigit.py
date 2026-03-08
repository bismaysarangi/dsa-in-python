def max_and_min_digit(n):
    max_digit = float('-inf')
    min_digit = float('inf')

    while n > 0:
        d = n % 10
        max_digit = max(max_digit, d)
        min_digit = min(min_digit, d)
        n //= 10
    
    print(max_digit, min_digit)

n = int(input())
max_and_min_digit(n)