clock = 1
sum_ = 0

with open('day10.txt') as f:
    x = 1
    checkpoint = 20
    line = f.readline()
    while line:
        a = line.strip("\n").split(" ")
        inc = 0
        if a[0] == "noop":
            #noop
            clock += 1
        else:
            #addi
            clock += 2
            inc = int(a[1])

        if clock > checkpoint:
            if (checkpoint == 100):
                print(x)
            sum_ += (x * checkpoint)
            checkpoint += 40
            x += inc
        else:
            x += inc

        line = f.readline()

print(sum_)