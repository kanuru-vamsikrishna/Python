"""
#Task

Your task is to implement a function which takes a string as input and return an object containing the properties vowels and consonants. The vowels property must contain the total count of vowels {a,e,i,o,u}, and the total count of consonants {a,..,z} - {a,e,i,o,u}. Handle invalid input and don't forget to return valid ones.

#Input

The input is any random string. You must then discern what are vowels and what are consonants and sum for each category their total occurrences in an object. However you could also receive inputs that are not strings. If this happens then you must return an object with a vowels and consonants total of 0 because the input was NOT a string. Refer to the Example section for a more visual representation of which inputs you could receive and the outputs expected. :)

Example:
Input: get_count('test')
Output: {vowels:1,consonants:3}

Input: get_count('tEst')
Output: {vowels:1,consonants:3}

Input get_count('    ')
Output: {vowels:0,consonants:0}

Input get_count()
Output: {vowels:0,consonants:0}
"""


import re
def getCount(words=None):
    "If no argument is passed, words will be None."
    normalizedWord = ''
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowelCount = 0
    if not isinstance(words, str) or words.strip() == "": # Check if input is not a string
        return {'vowels': 0, 'consonants': 0}
    else:
        normalizedWord = re.sub(r'[^a-zA-Z]', '', words).lower()
        for char in normalizedWord:
            if char in vowels:
               vowelCount += 1
                
    consonantsCount = len(normalizedWord) - vowelCount
    return { "vowels": vowelCount, "consonants": consonantsCount}

result = getCount('HEre Is sOme text')
print("Result:", result)