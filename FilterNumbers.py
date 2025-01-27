"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
def filter_list(l):
    i = 0
    array = []
    while i < len(l):
        if isinstance(l[i], (int, float)):
            array.append(l[i])
        i += 1
    return array

result = filter_list([1,2,'aasf','1','123',123])
print("Result:", result)

"""
isinstance(value, (int, float))  # Check for integer or float types
isinstance(value, int) # exclude numeric types like decimal.Decimal or complex numbers
isinstance(value, str) and value.isdigit() # If you need to detect whether a string contains a number:
"""