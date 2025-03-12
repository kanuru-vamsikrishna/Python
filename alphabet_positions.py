"""
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""

def alphabet_position(text):
    dictionary = {}
    array_list = []
    for i in range(97, 123): #ASCII range for a - z
        dictionary[chr(i)] = i - 96
    for x in list(text.split(" ")):
        for y in x:
            if y.lower() in dictionary.keys():
                array_list.append(str(dictionary.get(y.lower())))
    return " ".join(array_list)
    
result1 = alphabet_position("The sunset sets at twelve o' clock.")
result2 = alphabet_position("The narwhal bacons at midnight.")
print("Result1:", result1)
print("Result2:", result2)