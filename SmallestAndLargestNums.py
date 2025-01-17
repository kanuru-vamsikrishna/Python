"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
highAndLow("1 2 3 4 5"); // return "5 1"
highAndLow("1 2 -3 4 5"); // return "5 -3"
highAndLow("1 9 3 4 -5"); // return "9 -5"
"""

def high_and_low(numbers):
    array = numbers.split(" ")
    num = f"{max(array, key=int)} {min(array, key=int)}"
    return num

result = high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print("Result:", result)

"""
You’re getting the smallest and largest strings based on Python’s string comparison rules rather than based on the actual numeric value of each string.

In that case, the solution is to pass the built-in int() function as the key argument to min() and max(), like in the following examples:
follow more here: https://realpython.com/python-min-and-max/#:~:text=Use%20Python's%20min()%20and,any%20number%20of%20regular%20arguments
"""