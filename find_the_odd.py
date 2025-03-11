"""
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
"""

def find_outlier(integers):
    odd_list = []
    even_list = []
    for x in integers:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    return even_list[0] if len(even_list) == 1 else odd_list[0]
    
result1 = find_outlier([2, 4, 6, 8, 10, 3])
result2 = find_outlier([160, 3, 1719, 19, 11, 13, -21])
print("Result1:", result1)
print("Result2:", result2)