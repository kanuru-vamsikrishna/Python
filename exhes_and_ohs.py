"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):
    x = 0
    o = 0
    for y in s:
        if y == "x" or y == "X":
            x += 1
        elif y == "o" or y == "O":
            o += 1
    return True if x == o or o == 0 and x == 0 else False

result1 = xo("oxOx")
result2 = xo("zzoo")

print("Result1:", result1)
print("Result2:", result2)