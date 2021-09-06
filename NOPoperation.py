text =list(input())
new = []
index = 0
for i in range(0,2**25):
	if text[index].isupper() and i % 4 == 0:
		new.append(text.pop(0))
	elif text[index].islower():
		new.append(text.pop(0))
	else:
		new.append('NOP')
	if len(text) == 0:
		break
print(new.count('NOP'))
