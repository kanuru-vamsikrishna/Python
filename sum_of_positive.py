"""
[1, -4, 7, 12] => 
1
+
7
+
12
=
20
1+7+12=20
"""
def positive_sum(arr):
    sum = 0
    for x in arr:
        if x > 0:
            sum += x
        else:
            sum
    return sum

result = positive_sum([1,2,3,4,5])
print("Result:", result)