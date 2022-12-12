clock = 1
sum_ = 0
x = 1

WIDTH = 40
HEIGHT = 6

screen = []

for i in range(0 , HEIGHT):
    screen.append([])
    for j in range(0, WIDTH):
        screen[i].append('.')


with open('day10.txt') as f:
    line = f.readline()
    clock_goal = 0
    inc = 0
    while (line):
        #anaylze instruction, set up variables for later
        a = line.strip("\n").split(" ")
        if a[0] == "noop":
            #noop
            clock_goal += 1
            inc = 0
            line = " "
        elif a[0] == "addx":
            #addi
            clock_goal += 2
            inc = int(a[1])
            line = " "

        #crt
        col = (clock - 1) % WIDTH
        row = int((clock - 1) / WIDTH)

        c = set([x-1, x, x+1])
        if (col in c):
            screen[row][col] = "#"

        if (clock_goal == clock):
            x += inc
            line = f.readline()
        clock += 1

for i in range(0, len(screen)):
    print(' '.join([str(elem) for elem in screen[i]]))