"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1
2
+
2
2
+
2
2
=
9
1 
2
 +2 
2
 +2 
2
 =9.
"""

def square_sum(numbers):
    total = 0
    for x in numbers:
        total += x*x
    return total

def main():
    x = [1, 4, 6, 8]
    result = square_sum(x)
    print(f"Output: {result}")

main()