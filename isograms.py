"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
"""

def is_isogram(string):
    text = string.lower()
    array_list = list(text)
    processed = set()
    result = True
    for char in array_list:
        if char in processed:
            continue
        count = array_list.count(char)
        if count > 1:
            result = False
    return result

# Alternative way
def is_isogram(string):
    return len(string) == len(set(string.lower()))

result = is_isogram("Dermatoglyphics")
print("Result:", result)