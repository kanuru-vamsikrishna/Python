"""
Task:
You have to write a function pattern which creates the following pattern up to n/2 number of lines.

If n <= 1 then it should return "" (i.e. empty string).
If any odd number is passed as argument then the pattern should last up to the largest even number which is smaller than the passed odd number.
Examples:
n = 8:

22
4444
666666
88888888
n = 5:

22
4444
"""

def pattern(n):
    output = ''
    i = 0
    if n <= 1:
        return output
    else:
        number = n if n % 2 == 0 else n - 1
        while i <= number:
            if i != 0 and i % 2 == 0:
                output += f"{str(i) * i}" + ('' if i == number else '\n')
            i += 1
    return output

"""
str(i): Converts the integer i to its string representation.
str(i) * i: Repeats the string representation of i, i times.
f"{...}": Embeds the resulting string into an f-string.
"""

result = pattern(5)
print("Result:", result)