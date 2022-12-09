import math

tail_positions = set([])
tail_positions.add(tuple([0,0]))
rope = [[0,0] for i in range(0, 10)]


def calculateNewBack(front, back, incx, incy):
    xdis = front[0] - back[0]
    ydis = front[1] - back[1]
    d = ''
    if abs(xdis) == abs(ydis):
        if xdis > 0 and ydis > 0:
            d = 'urdi'
        elif xdis > 0 and ydis < 0:
            d = 'drdi'
        elif xdis < 0 and ydis < 0:
            d = 'dldi'
        elif xdis < 0 and ydis > 0:
            d = 'uldi'
    else:
        if abs(xdis) == 2:
            if xdis > 0:
                d = 'r'
            else:
                d = 'l'
        if abs(ydis) == 2:
            if ydis > 0:
                d = 'u'
            else:
                d = 'd'
    calculateDiagonal(front, back, d)

def calculateDiagonal(front, back, direction):
    if direction == 'r':
        #right
        back[0] = front[0] - 1
        back[1] = front[1]
    elif direction == 'l':
        #left
        back[0] = front[0] + 1
        back[1] = front[1]
    elif direction == 'u':
        #up
        back[0] = front[0]
        back[1] = front[1] - 1
    elif direction == 'd':
        #down
        back[0] = front[0]
        back[1] = front[1] + 1
    elif direction == 'urdi':
        back[0] = front[0] - 1
        back[1] = front[1] - 1        
    elif direction == 'dldi':
        back[0] = front[0] + 1
        back[1] = front[1] + 1  
    elif direction == 'uldi':
        back[0] = front[0] + 1
        back[1] = front[1] - 1        
    elif direction == 'drdi':
        back[0] = front[0] - 1
        back[1] = front[1] + 1  

def updateBack(idx, incx, incy):
    front = rope[idx - 1]
    back = rope[idx]
    #update back
    e = front[0] - back[0]
    f = front[1] - back[1]
    c = math.sqrt((e*e) + (f*f))
    if (c > math.sqrt(2)):
        calculateNewBack(front, back, incx, incy)
        if (idx == len(rope) - 1):
            tail_positions.add(tuple(back))

def updateFront(idx, incx, incy):
    front = rope[idx]
    front[0] += incx
    front[1] += incy

with open('day9.txt') as file:
    line = file.readline()
    while line:
        a = line.split(" ")
        b = int(a[1])
        dist = [0, 0]
        if (a[0] == 'D'):
            dist[1] -= b
        if (a[0] == 'U'):
            dist[1] += b
        if (a[0] == 'L'):
            dist[0] -= b
        if (a[0] == 'R'):
            dist[0] += b

        for i in range(0, b):
            updateFront(0, int(dist[0]/b), int(dist[1]/b))
            for j in range(1, len(rope)):
                updateBack(j, int(dist[0]/b), int(dist[1]/b))
        line = file.readline()

'''
grid = []
SIZE = 30
for i in range(0, SIZE):
    grid.append([])
    for j in range(0, SIZE):
        grid[i].append('.')

grid[10][10] = 's'

for i in range(0, len(rope)):
    point = rope[i]
    offsetx = 10
    offsety = 10
    grid[SIZE - point[1] - offsety][point[0] + offsetx] = str(i)

for i in range(0, SIZE):
    print(grid[i])
'''

print(len(tail_positions))