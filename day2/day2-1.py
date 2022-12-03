PLAYER1 = ['A', 'B', 'C'] #rock, paper, scissors
PLAYER2 = ['X', 'Y', 'Z']
score = 0

def determineWinner(a, b):
    if (a == b):
        return 1
    c = (a + 1) % 3
    if (b == c):
        return 2
    return 0


with open('day2.txt') as f:
    line = f.readline()
    while line:
        a = PLAYER1.index(line[0:1])
        b = PLAYER2.index(line[2:3])
        score += (3*determineWinner(a, b)) + (b+1)
        line = f.readline()

print("Part 1: {}".format(score)) #part 1
