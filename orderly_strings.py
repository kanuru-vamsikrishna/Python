"""
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

def order(sentence):
    split_sentence = sentence.split(" ")
    array = []
    for x in range(1, 10):
        if len(sentence) == 0:
            return ""
        else:
            for sen in split_sentence:
                if str(x) in sen:
                    array.append(sen)
    return " ".join(array)
    
result1 = order("is2 Thi1s T4est 3a")
result2 = order("4of Fo1r pe6ople g3ood th5e the2")

print("Result1:", result1)
print("Result2:", result2)