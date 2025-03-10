"""
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
"""

def get_middle(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 == 1 else s[mid - 1: mid + 1]

result1 = get_middle("middle") 
result2 = get_middle("KVamsiKrishna")
print("Result1:", result1)
print("Result2:", result2)