# import this
from collections import Counter

# Variables and some arithmetic
a = 885
b = 950
print(f"{a}^2 + {b}^2 = {a**2 + b**2}")

# Strings and lists
wordOneStartPos = 87
wordOneEndPos = 91

wordTwoStartPos = 123
wordTwoEndPos = 133

txtStr = "yyEMIUH5v1g3eXfY84Qsy0UXpoR33tR7vGNVBThSPuD2FSK2p56TVXrtV4vZnmC7RVi9KYWcKP7kL2yBSSS0tSuSaigahI8W6gjY8xjsnZ19zk73WfbOpJGQ5sUbukhunensisVin4HYE3WeyepM7UYCcjd0ltv0RpAaDkhDzW5Mdj4cNlzRE."
# end position is not inclusive so we add 1
print(f"{txtStr[wordOneStartPos: wordOneEndPos +1]} {txtStr[wordTwoStartPos: wordTwoEndPos +1]}")


# Conditions and loops
startPos = 4476
endPos = 8755
result = 0

for x in range(startPos, endPos + 1):
    if x % 2 != 0:
        result += x

# result = [x for x in range(startPos, endPos + 1)  if x % 2 != 0] all values listed
# result = sum([x for x in range(startPos, endPos + 1)  if x % 2 != 0]) same result
print(result)


# Working with files
outputfile = []

with open('village/input.txt', 'r') as f:
    outputfile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]
    
with open('village/output.txt', 'w') as f:
    f.write(''.join([line for line in outputfile]))


# Dictionaries
text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

wordCountDict = {}

for word in text.split(' '):
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

# wordCountDict = Counter(text.split(' '))

for key, value in wordCountDict.items():
    print(key, value)