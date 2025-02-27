def solution(number):
    array = []
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            array.append(x)
    return sum(array)

result = solution(18)
print("Result:", result)