import math

tail_positions = set([])
tail_positions.add(tuple([0,0]))
tail = [0, 0]
head = [0, 0]

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
            prev_h_x = head[0]
            prev_h_y = head[1]
            head[0] += int((dist[0]/b))
            head[1] += int((dist[1]/b))
            #update tail
            e = head[0] - tail[0]
            f = head[1] - tail[1]
            c = math.sqrt((e*e) + (f*f))
            if (c > math.sqrt(2)):
                tail[0] = prev_h_x
                tail[1] = prev_h_y
                tail_positions.add(tuple(tail))

        print(head)
        print(tail)
        line = file.readline()

print(tail_positions)
print(len(tail_positions))