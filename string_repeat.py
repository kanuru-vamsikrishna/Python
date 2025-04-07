"""
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""

def repeat_str(repeat, string):
    return string * repeat

result = repeat_str(3, "vamsi")
print("Result:", result)