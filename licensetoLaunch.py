number_of_days = int(input())
space_junks = list(map(int,input().split(' ')))
least = min(space_junks)
count = 0
for i in range(0,len(space_junks)):
	if space_junks[i] == least:
		count = i
		break
	try:
		if space_junks[i] == space_junks[i+1]:
			count = i
			break
	except IndexError:
		print('error at',i)
		break
print(count)