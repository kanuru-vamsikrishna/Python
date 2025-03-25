"""
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

def descending_order(num):
    lis = list(str(num))
    array = []
    lis.sort(reverse=True)
    for x in lis:
        array.append(int(x))
    result = int("".join(map(str, array)))
    return int(result)
        
result = descending_order(123456789)
print("Result:", result)