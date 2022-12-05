all_crates = [[] for i in range(0, 9)]

for line in reversed(open("stack.txt").readlines()):
    for i in range(0, 9):
        if (line[(4*i + 1)] != " "):
            all_crates[i].append(line[(4*i + 1)])

with open('day5.txt') as f:
    line = f.readline()
    while line:
        a = line.split(" ")
        count = int(a[1])
        fromth = int(a[3]) - 1
        toth = int(a[5]) - 1

        for i in range(0, count):
            all_crates[toth].append(all_crates[fromth].pop())

        line = f.readline()


res = ""
for i in range(0, 9):
    res += all_crates[i].pop()

print(res)