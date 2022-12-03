result = 0

def determineLetter(a, b, c):
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            for u in range(0, len(c)):
                if (a[i] == b[j] == c[u]):
                    return a[i]

def getPriority(letter):
    if (ord(letter) < ord('a')):
        return (ord(letter) - ord('A') + 27)
    else:
        return (ord(letter) - ord('a') + 1)


f = open('day3.txt', 'r')
lines = f.read().strip().split("\n")

for i in range(0, int(len(lines) / 3)):
    #letter = determineLetter(lines[i*3], lines[i*3 + 1], lines[i*3 + 2])
    letter = (set(lines[i*3]) & set(lines[i*3 + 1]) & set(lines[i*3 + 2])).pop()
    result += getPriority(letter)

print("Day 3 Result: {}".format(result)) # Part 2