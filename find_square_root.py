"""
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""

import math
def is_square(n):
    if n < 0:
        return False
    elif math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
        return True
    else:
        return False

result = is_square(25)
print("Result:", result)