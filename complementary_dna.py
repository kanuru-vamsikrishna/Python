"""
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
"""

def DNA_strand(dna):
    string = []
    for x in list(dna):
        if x == "A":
            string.append(x.replace("A", "T"))
        elif x == "T":
            string.append(x.replace("T", "A"))
        elif x == "C":
            string.append(x.replace("C", "G"))
        elif x == "G":
            string.append(x.replace("G", "C"))
    return "".join(string)
        
result = DNA_strand("ATTGC")
print("Result:", result)