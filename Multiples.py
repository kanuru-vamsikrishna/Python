"""
Problem Statement
Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3, "Boom" if it is divisible by 5, "BangBoom" if it divisible by 3 and 5, and "Miss" if it isn't divisible by any of them. Note: Your program should only return one value

Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 --> Output: "Boom"
"""

def multiple(x):
    if x%3 == 0 and x%5 == 0:
      return 'BangBoom'
    elif x%3 == 0:
      return 'Bang'
    elif x%5 == 0:
      return 'Boom'
    else:
      return 'Miss'

def main():
    x = 105
    result = multiple(x)
    print(f"Output: {result}")

main()

    
