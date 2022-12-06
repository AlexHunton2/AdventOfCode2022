res = -1
SIZE = 4
line = open("day6.txt").readline()
a = []
for i in range(0, SIZE):
	a.append(line[i])
c = set(a)
for i in range(1, len(line)):
	c = set(line[i:i+SIZE])
	if (len(c) == SIZE):
		res = i
		break;
print(res+SIZE)