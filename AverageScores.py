"""
Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number. You are not allowed to use any loops (including for, for/in, while, and do/while loops).

The array will never be empty.
"""

def average(scores):
    result = round(sum(scores) / len(scores))
    return result

def main():
    x = [1, 1, 1, 1, 9999]
    result = average(x)
    print(f"Output: {result}")

main()