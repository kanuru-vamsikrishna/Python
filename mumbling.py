"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(st):
    array = []
    i = 0
    while i < len(st):
        each_string = st[i] * (i + 1)
        array.append(each_string.title())
        i += 1
    return "-".join(array)

result1 = accum("ZpglnRxqenU")
result2 = accum("NyffsGeyylB")
print("Result1:", result1)
print("Result2:", result2)