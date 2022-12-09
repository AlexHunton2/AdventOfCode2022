trees = []

with open('day8.txt') as f:
    line = f.readline()
    while line:
        line = line.strip("\n")
        trees.append([int(n) for n in line])
        line = f.readline()

def isVisible(ri, ci):
    top = isVisibleRow(ri, ci, -1, -1)
    bottom = isVisibleRow(ri, ci, 1, len(trees))
    left = isVisibleCol(ri, ci, -1, -1)
    right = isVisibleCol(ri, ci, 1, len(trees[0]))
    if (top or bottom or left or right):
        return 1
    return 0

def isVisibleRow(ri, ci, inc, size):
    i = ri + inc
    start_value = trees[ri][ci]
    while (i != size):
        if (trees[i][ci] >= start_value):
            return False
        i += inc
    return True

def isVisibleCol(ri, ci, inc, size):
    i = ci + inc
    start_value = trees[ri][ci]
    while (i != size):
        if (trees[ri][i] >= start_value):
            return False
        i += inc
    return True


count = 0
for row in range(0, len(trees)):
    for col in range(0, len(trees[row])):
        count += isVisible(row, col)
print(count)