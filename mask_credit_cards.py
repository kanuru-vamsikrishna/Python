"""
"4556364607935616" --> "############5616"
"""
def maskify(cc):
    hash = (len(cc) - 4) * "#"
    return hash + cc[-4:]
        
result = maskify("4556364607935616")
print("Result:", result)