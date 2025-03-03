"""
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.

"""

def first_non_repeating_letter(s):
    mini_text = list(s)
    count_dict = {}
    for each_element in mini_text:
        lower_element = each_element.lower()
        count_dict[lower_element] = count_dict.get(lower_element, 0) + 1
    for each_element in mini_text:
        if count_dict[each_element.lower()] == 1:
            return each_element

    return ''

result1 = first_non_repeating_letter("sTreSS")
result2 = first_non_repeating_letter("hello world, eh?")
print("Result1:", result1)
print("Result2:", result2)