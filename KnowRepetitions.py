"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""

def duplicate_count(text):
    text = text.lower()
    mini_text = list(text)
    array = []
    processed = set()
    
    for char in mini_text:
        if char in processed:
            continue
        count = mini_text.count(char)
        if count > 1:
            array.append({"char": char, "count": count})
        processed.add(char)
    return len(array)

result = duplicate_count("Indivisibilities")
print("Result:", result)

"""
set() in Python does not mean declaring an object in the sense of creating a generic object (as in JavaScript or other object-oriented languages). Instead, a set in Python is a built-in data type that represents an unordered collection of unique elements.

Key Features of set in Python:
Unordered: The elements in a set have no specific order.
Unique Elements: A set cannot contain duplicate elements.
Efficient Membership Testing: Testing whether an element is in a set (using in) is faster compared to lists because set uses a hash table internally.
Mutable: You can add or remove elements from a set.
"""