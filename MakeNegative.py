"""
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
"""

def make_negative( number ):
    if number < 0:
        return number
    else:
        return -number
    
result = make_negative(-9)
print("Result:", result)

# -abs(number) is an inbuilt method