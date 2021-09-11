from itertools import combinations as combine
'''first find all the possible combinations
second get the sum and assign to the bit index and it already exists print that index sets and the current set and break'''
# It is easy if you have knowledge of bitmasking
testcase = int(input())
for i in range(testcase):
	numbers = list(map(int,input().split(' ')))
	length = numbers.pop(0)
	new = []
	inde = []
	count = 0
	for j in range(1,length+1):
		to_find = combine(numbers,j)
		for item in to_find:
			idx = sum(item)
			if idx not in inde:
				inde.append(idx)
				new.append(item)
			else:
				count += 1
				print(f'Case #{i+1}:')
				print(' '.join(list(map(str,item))))
				print(' '.join(list(map(str,new[inde.index(idx)]))))
				break
		if count > 0:
			break		
	else:
		print('impossible')
