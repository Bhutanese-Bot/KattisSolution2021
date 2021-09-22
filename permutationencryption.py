while True:
	length,*permute = map(int,input().split(' '))
	if length == 0:
		break
	text = list(input())
	container = [text[i:i+length]for i in range(0,len(text),length)]
	for i in range(0,len(container)):
		if len(container[i]) != length:
			append_till = length-len(container[i])
			for j in range(append_till):
				container[i].append(' ')
	text = ''
	for i in range(0,len(container)):
		for j in range(length):
			text = text + container[i][permute[j]-1]
	print("'"+text+"'")
