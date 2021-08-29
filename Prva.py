row,coloumn = map(int,input().split(' '))
quest = []
for i in range(row):
	words = list(input())
	quest.append(words)
transpose = list(zip(*quest)) #transpose the matrix to get the words
transpose = [''.join(item) for item in transpose]
quest = [''.join(item) for item in quest]
answer_bank = []
for item in quest:
	if '#' in item: #split the words separated by hash
		lst = item.split('#')
		for word in lst:
			if len(word) > 1:
				answer_bank.append(word)
	else:
		answer_bank.append(item)
for item in transpose:
	if '#' in item:
		lst = item.split('#')
		for word in lst:
			if len(word) > 1:
				answer_bank.append(word)
	else:
		answer_bank.append(item)
answer_bank = sorted(answer_bank)
print(answer_bank[0])
