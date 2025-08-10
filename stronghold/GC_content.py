def readFile(filepath):
    with open(filepath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


# storing file content in a list
FASTAFile = readFile("test_data/gc_content.txt")
# dictionary for labels + data
FASTADict = {}
# string for holding to current label
FASTALabel = ""

# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# Using dictionary comprehension to generate a new dictionary with GC content
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

# Looking for max value in values() of our a new dictionary
MAXGCKey = max(RESULTDict, key=RESULTDict.get)

# printing rosalind formatted result
print(f"{MAXGCKey[1:]}\n{RESULTDict[MAXGCKey]}")
