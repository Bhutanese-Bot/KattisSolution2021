def read():
	return int(input())
def find_min(x,y):
	if x>y:
		return y
	else:
		return x
testcase = read()
case = 0
for j in range(testcase):
	case += 1
	S = read()
	segments = input().split(' ')
	red = []
	blue = []
	for item in segments:
		if 'R' in item:
			red.append(item)
		else:
			blue.append(item)
	for j in range(0,len(red)):
		num = ''
		for i in range(0,len(red[j])):
			if red[j][i].isdigit():
				num += red[j][i]
		red[j] = int(num)
	for j in range(0,len(blue)):
		num = ''
		for i in range(0,len(blue[j])):
			if blue[j][i].isdigit():
				num += blue[j][i]
		blue[j] = int(num)
	red = sorted(red,reverse=True)
	blue = sorted(blue,reverse=True)
	print(red)
	print(blue)
	if len(red) == 0 or len(blue) == 0:
		print(f'Case #{case}: {0}')
	else:
		mini = find_min(len(red),len(blue))
		longest = 0
		for i in range(0,mini):
			l1 = red[i] - 1
			l2 = blue[i] - 1
			if l1 < 0:
				l1 = 0
			if l2 < 0:
				l2 = 0
			longest += (l2+l1)
		print(f'Case #{case}: {longest}')


