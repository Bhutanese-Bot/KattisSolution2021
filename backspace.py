letters = list(input())
only_alpha = []
for item in letters:
	if item.isalpha():
		only_alpha.append(item)
	else:
		only_alpha.pop()
print(''.join(only_alpha))