"""
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
"""

def summation(num):
    i = 1
    count = 0
    while i <= num:
        count += i
        i += 1
    return count
    
result = summation(24)
print("Result:", result)