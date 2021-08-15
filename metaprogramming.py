from sys import stdin
myDict = {}
for line in stdin:
	if line == '':
		break
	line = line.rstrip().lstrip()
	if line.startswith('define'):
		defi,number,const = line.split(' ')
		myDict[const] = int(number)
	else:
		evalu,name,operator,name2 = line.split(' ')
		try:
			if operator == '<':
				boolean = myDict[name] < myDict[name2]
			elif operator == '=':
				boolean = myDict[name] == myDict[name2]
			else:
				boolean = myDict[name] > myDict[name2]
			if boolean == True:
				boolean = 'true'
			else:
				boolean = 'false'
			print(boolean)
		except KeyError:
			print('undefined')