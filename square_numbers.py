def square_digits(num):
    return int(''.join(str(int(x)**2) for x in str(num)))

result = square_digits(12345)
print("Result:", result)