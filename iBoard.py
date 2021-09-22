from sys import stdin
one = False 
zero = False
for line in stdin:
	if line == '':
		break
	line = line.strip()
	chars = list(line)
	for item in chars:
		item = ord(item)
		binary = bin(item)
		binary = binary[2:]
		binary = list(map(int,list(binary)))
		binary = binary[::-1]
		if len(binary) != 7:
			while True:
				binary.append(0)
				if len(binary) == 7:
					break
		for zeroone in binary:
			if zeroone == 1:
				if one == False:
					one = True
				else:
					one = False
			else:
				if zero == True:
					zero = False
				else:
					zero = True
	if one == True or zero == True:
		print('trapped')
	else:
		print('free')
	one = False
	zero = False
