from sys import stdin

for line in stdin:
	if line == '':
		break
	symbols = [chr(i) for i in range(33,43)]
	for i in range(91,94):
		symbols.append(chr(i))
	levels = int(line)
	text = list(input())
	new = []
	for j in range(levels):
		for i in range(len(text)):
			if i == 0 and text[i] in symbols:
				new.append('\\')
				new.append(text[i])
			if i == 0 and text[i] not in symbols:
				new.append(text[i])
			if i != 0:
				if text[i] in symbols:
					new.append('\\')
					new.append(text[i])
				else:
					new.append(text[i])
		text = new[:]
		new.clear()
	print(''.join(text))
