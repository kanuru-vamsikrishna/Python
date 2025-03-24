"""
Sam Harris => S.H

patrick feeney => P.F
"""

def abbrev_name(name):
    list_of_names = name.split()
    i = 0
    array = []
    while i < len(list_of_names):
        array.append(list_of_names[i][0].upper())
        i += 1
    return ".".join(array)

result1 = abbrev_name("Sam Harris")
result2 = abbrev_name("Kanuru Vamsi Krishna")

print("Result1:", result1)
print("Result2:", result2)
