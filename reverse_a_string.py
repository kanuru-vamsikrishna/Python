"""
"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
"""

def spin_words(sentence):
    array = []
    for x in sentence.split(" "):
        if len(x) >= 5:
            array.append(''.join(reversed(x)))
        else:
            array.append(x)
    final_string = " ".join(array)
    return final_string

result = spin_words("This sentence is a sentence")
print("Result:", result)