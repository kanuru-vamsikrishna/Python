"""
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""

def unique_in_order(sequence):
    res = [sequence[i] for i in range(len(sequence)) if i == 0 or sequence[i] != sequence[i - 1]]
    return res

result1 = unique_in_order("AAAABBBCCDAABBB")
result2 = unique_in_order([1, 2, 2, 3, 3])
print("Result1:", result1)
print("Result2:", result2)