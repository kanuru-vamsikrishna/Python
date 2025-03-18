"""
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
"""

import math

def narcissistic(value):
    def calculate_value(new_value):
        narcissist_value = 0
        i = 0
        length = len(new_value)
        
        while i < length:
            narcissist_value += int(new_value[i]) ** length
            i += 1
        return int(narcissist_value) == value  

    return True if len(str(value)) == 1 else calculate_value(list(str(value)))

result1 = narcissistic(122)
result2 = narcissistic(153)

print("Result1:", result1)
print("Result2:", result2)