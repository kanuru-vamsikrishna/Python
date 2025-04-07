"""
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""

def to_jaden_case(string):
    list = [word[0].upper() + word[1:].lower() for word in string.split()]
    return " ".join(list)

result = to_jaden_case("How can mirrors be real if our eyes aren't real")
print("Result:", result)