result = 0

def determineLetter(a, b):
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if (a[i] == b[j]):
                return a[i]

with open('day3.txt') as f:
    line = f.readline()
    while line:
        m = int(len(line) / 2)
        first = line[0:m]
        second = line[m::]
        letter = determineLetter(first, second)

        if (ord(letter) < ord('a')):
            result += (ord(letter) - ord('A') + 27)
        else:
            result += (ord(letter) - ord('a') + 1)

        line = f.readline()

print("Day 3 Result: {}".format(result)) # Part 1