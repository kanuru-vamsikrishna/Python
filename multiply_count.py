"""
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
"""

def persistence(n):
    count = 0
    while n >= 10:
        multiple_result = 1

        for digit in str(n):
            multiple_result *= int(digit)
        
        n = multiple_result
        count += 1

    return count

result1 = persistence(999)
result2 = persistence(9876)
print("Result1:", result1)
print("Result2:", result2)