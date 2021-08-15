from sys import stdin
myDict = {}
for line in stdin:
	new = line.split(' ')
	if line == "":
		break
	elif len(new) > 1:
		g = line.rstrip().lstrip()
		new = g.split(' ')
		myDict[new[1]] = new[0]
	elif line == "\n":
		pass
	else:
		l = line.rstrip().lstrip()
		try:
			print(myDict[l])
		except KeyError:
			print('eh')

