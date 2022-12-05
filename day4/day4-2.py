count = 0

with open('day4.txt') as f:
    line = f.readline()
    while line:
        pairs = line.split(",")
        a = [int(c) for c in pairs[0].split("-")]
        b = [int(c) for c in pairs[1].split("-")]
        
        u = []
        for i in range(a[0], a[1]+1):
            u.append(i)
        v = []
        for i in range(b[0], b[1]+1):
            v.append(i)

        if (set(u) & set(v) != set([])):
            count += 1
        line = f.readline()

print("Part 2: {}".format(count))