"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    string = s.split()
    list = []
    for x in string:
        list.append(len(x))
    return min(list)

result = find_short("turns out random test cases are easier than writing out basic ones")
print("Result:", result)