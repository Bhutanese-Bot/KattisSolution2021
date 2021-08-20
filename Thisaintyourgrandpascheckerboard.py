N = int(input())
List1 = []
for i in range(N):
	pos = input()
	List1.append(list(pos))
List2 = list(zip(*List1))
List2 = [list(List2[i]) for i in range(len(List2))]
count = 0
for i in range(N):
	for j in range(1,len(List1[i])):
		try:
			if List1[i][j-1] == 'B' and List1[i][j] == 'B' and List1[i][j+1] == 'B':
				count += 1
			if List1[i][j-1] == 'W' and List1[i][j] == 'W' and List1[i][j+1] == 'W':
				count += 1
			if List2[i][j-1] == 'B' and List2[i][j] == 'B' and List2[i][j+1] == 'B':
				count += 1
			if List2[i][j-1] == 'W' and List2[i][j] == 'W' and List2[i][j+1] == 'W':
				count += 1
		except IndexError:
			pass
if count > 0:
	print(0)
else:
	inner_count = 0
	for i in range(0,len(List1)):
		if List1[i].count('W')!=List1[i].count('B'):
			inner_count += 1
		if List2[i].count('W')!=List2[i].count('B'):
			inner_count += 1
	if inner_count > 0:
		print(0)
	else:
		print(1)
		
