from sys import stdin
myDict = dict()
for line in stdin:
	List = []
	if line ==' ':
		break
	Line = line.rstrip().lstrip()
	k = Line.split(' ')
	for item in k:
		if item.lower() not in myDict:
			myDict[item.lower()] = 1
			List.append(item)
		else:
			myDict[item.lower()] += 1
			List.append('.')
	print(' '.join(List))