"""
'world'  =>  'dlrow'
'word'   =>  'drow'
"""

def solution(string):
    res = "".join(reversed(string))
    return res

result = solution('world')
print("Result:", result)