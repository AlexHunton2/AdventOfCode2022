class Directory:
	def __init__(self, name, _dir):
		self._name = name
		self._dir =  _dir

	def addFile(self, name, size):
		self._dir.append(File(name, size))

	def addDir(self, name, _dir):
		self._dir.append(Directory(name, _dir))


class File:
	def __init__(self, name, size):
		self._name = name
		self._size = size

file_system = [Directory("/", [])]
curr_dir = file_system[0]
prev_dir = []

isCommandPhase = True
with open('day7.txt') as f:
    line = f.readline()
    while line:
    	a = line.split(" ")
    	if isCommandPhase:
    		if line[2:4] == 'cd':
    			# change directory phase
    			if (a[2][0:2] == '..'):
    				curr_dir = prev_dir.pop()
    			else:
	    			for i in range(0, len(curr_dir._dir)):
	    				if (curr_dir._dir[i]._name == a[2]):
	    					prev_dir.append(curr_dir)
	    					curr_dir =  curr_dir._dir[i]
	    					break
    		else:
    			# change to add phase
    			isCommandPhase = False
    	else:
    		if a[0] == 'dir':
    			# add directory to where we are
    			curr_dir.addDir(a[1], [])
    		else:
    			# add file to where we are
    			curr_dir.addFile(a[1], int(a[0]))
    	line = f.readline()
    	if line:
	    	if line[0] == "$":
	    		isCommandPhase = True

res = 0

def searchTree(_dir, count):
	global res
	for i in range(0, len(_dir)):
		if isinstance(_dir[i], File):
			count += _dir[i]._size

	for i in range(0, len(_dir)):
		if isinstance(_dir[i], Directory):
			count += searchTree(_dir[i]._dir, 0)

	if (count < 100000):
		res += count

	return count

searchTree(file_system[0]._dir, 0)
print(res)
    