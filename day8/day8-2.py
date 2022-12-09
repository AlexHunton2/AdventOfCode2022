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
    return top * bottom * left * right

def isVisibleRow(ri, ci, inc, size):
    i = ri + inc
    c = 0
    start_value = trees[ri][ci]
    while (i != size):
        c += 1
        if (trees[i][ci] >= start_value):
            break
        i += inc
    return c

def isVisibleCol(ri, ci, inc, size):
    i = ci + inc
    c = 0
    start_value = trees[ri][ci]
    while (i != size):
        c += 1
        if (trees[ri][i] >= start_value):
            break
        i += inc
    return c


values = []
for row in range(0, len(trees)):
    for col in range(0, len(trees[row])):
        values.append(isVisible(row, col))
print(max(values))