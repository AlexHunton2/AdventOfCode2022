COL1 = ['A', 'B', 'C'] #rock, paper, sci
COL2 = ['X', 'Y', 'Z']
score = 0

def determineDecision(a, b): #opponent, result
    if (b == 2): # return winner
        return(a + 1) % 3
    if (b == 1): # 1 must be draw
        return a;
    if (b == 0): # return loser
        return (a + 2) % 3

with open('day2.txt') as f:
    line = f.readline()
    while line:
        a = COL1.index(line[0:1])
        b = COL2.index(line[2:3])
        score += ((3*b) + (determineDecision(a, b) + 1))
        line = f.readline()

print("Part 2: {}".format(score)) #part 2
